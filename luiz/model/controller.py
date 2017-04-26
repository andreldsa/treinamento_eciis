
from models import *

class OpracoesInstituicao(object):

    def criarInstituicao(self, nome_instituicao, nome_resposavel, cpnj, natureza, endereco, area_atuacao,  email_contato, telefone_contato, descricao=None):

        instituicao = Instituicao()

        instituicao.nome_instituicao = nome_instituicao
        instituicao.nome_resposavel = nome_resposavel
        instituicao.cpnj = cpnj
        instituicao.natureza = natureza
        instituicao.endereco = endereco
        instituicao.area_atuacao = area_atuacao
        instituicao.descricao = descricao
        instituicao.email_contato = email_contato
        instituicao.telefone_contato = telefone_contato

        instituicao.put()

    def buscarInstituicaoPorNome(self, nome_instituicao_buscada):

        busca = Instituicao.query()
        busca = busca.filter(Instituicao.nome_instituicao == nome_instituicao_buscada)

        return busca.fetch()

    def buscarTodasAsInstituicoes(self):
        busca = Instituicao.query()
        return busca.fetch()

class OperacoesUser(object):

    def cadastrarUsuario(self, nome, senha, cpf, email):
        usuario = User(id = cpf)

        usuario.nome = nome
        usuario.senha = senha
        usuario.cpf = cpf
        usuario.email = email

        usuario.put()


class OperacoesPost(object):

    def criarPost(self, nome_instituicao, nome_autor, num_curtidas):

        post = Post()

        post.nome_instituicao = nome_instituicao
        post.nome_autor = nome_autor
        post.num_curtidas = num_curtidas

        post.put()
