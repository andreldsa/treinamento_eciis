# coding: utf-8
import datetime
import md5

from google.appengine.ext import ndb
from google.appengine.api import memcache

def project_state(projeto):
    today = datetime.date
    if today < projeto.inicio_at:
        return 'pending'
    elif projeto.inicio_at < today <= (projeto.fim_at or today):
        return 'ongoing'
    
    return 'finished'


def gravatar_url(email):
    email_lower = email.lower().strip()
    hash_md5 = md5.md5(email_lower)
    return "http://www.gravatar.com/avatar/%s.jpg" % hash_md5.hexdigest()


class Projeto(ndb.Model):
    nome = ndb.StringProperty(required=True)
    coordenador = ndb.StringProperty(required=True)
    participantes = ndb.StringProperty(repeated=True)
    gerente = ndb.KeyProperty(kind='Perfil')
    inicio_at = ndb.DateProperty(required=True)
    fim_at = ndb.DateProperty()
    state = ndb.ComputedProperty(project_state)

    @staticmethod
    def get_all(add=[], remove=[]):
        query = Projeto.query()
        data = []
        for projeto in query.fetch():
            pdict = projeto.to_dict() 
            for prop in add:
                pdict[prop] = getattr(projeto, prop)
            for prop in remove:
                del pdict[prop]
            data.append(pdict)

        return data

    @property
    def url(self):
        return 'http://localhost:8080/api/projetos/%s' % self.key.urlsafe()


class Vinculo(ndb.Model):
    projeto = ndb.KeyProperty(kind='Projeto')
    funcao = ndb.StringProperty()
    inicio_at = ndb.DateProperty(required=True)
    fim_at = ndb.DateProperty()
    sala = ndb.StringProperty()
    state = ndb.StringProperty(choices=set([
        'draft', # todos os dados livres para editar (inclusive vínculo removível)
        'ongoing', # dados básicos confirmados pelo gerente, inicio e projeto fixados
        'ended', # todos os dados confirmados pelo gerente; todos os dados bloqueados
    ]))

    @staticmethod
    def create(vdata):
        vinculo = Vinculo()
        vinculo.projeto = ndb.Key(urlsafe=vdata['projeto'])
        vinculo.funcao = vdata['funcao']
        inicio_at = vdata['inicio_at'].split("T")[0].split(" ")[0]
        vinculo.inicio_at = datetime.datetime.strptime(inicio_at, '%Y-%m-%d')
        if vdata['fim_at']:
            vinculo.fim_at = datetime.datetime.strptime(inicio_at, '%Y-%m-%d')
            fim_at = vdata['fim_at'].split("T")[0].split(" ")[0]
            vinculo.fim_at = datetime.datetime.strptime(fim_at, '%Y-%m-%d')
        if vdata['fim_at']:
            vinculo.fim_at = datetime.datetime.strptime(fim_at, '%Y-%m-%d')
            vinculo.sala = vdata['sala']
        return vinculo


class Perfil(ndb.Model):

    # personal data 1
    nome = ndb.StringProperty()
    data_nascimento = ndb.DateProperty()
    lattes = ndb.StringProperty()
    cpf = ndb.StringProperty()
    vinculo_ufcg = ndb.StringProperty(choices=set([
        'graduando',
        'mestrando',
        'doutorando',
        'professor',
        'servidor',
    ]))

    # personal data 2
    fones = ndb.JsonProperty()
    endereco = ndb.StringProperty()
    emails = ndb.StringProperty(repeated=True)
    gravatar_url = ndb.StringProperty()

    # splab related data 
    #usernames = ndb.JsonProperty()
    cartao_acesso = ndb.StringProperty()
    vinculos = ndb.LocalStructuredProperty(Vinculo, repeated=True)

    # meta data: last time the user checked the data
    created_at = ndb.DateTimeProperty(auto_now_add=True)
    checked_at = ndb.DateTimeProperty()


    @staticmethod
    def get_by_email(email):
        query = Perfil.query(Perfil.emails == email.lower())
        perfil = query.get()
        return perfil


    def update(self, data):
        for prop in ['nome', 'cpf', 'lattes', 'vinculo_ufcg', 'endereco']:
            setattr(self, prop, data.get(prop))
        
        if 'data_nascimento' in data:
            data_nascimento = data['data_nascimento'].split("T")[0].split(" ")[0]
            self.data_nascimento = datetime.datetime.strptime(data_nascimento, '%Y-%m-%d')

        self.fones = data['fones']
        self.emails = data['emails']
        self.cartao_acesso = data['cartao_acesso']
        self.vinculos = [Vinculo.create(vdata) for vdata in data['vinculos']]
        self.gravatar_url = gravatar_url(self.emails[0])

