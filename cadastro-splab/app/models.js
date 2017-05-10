"use strict";

function User() {
}

function Perfil(data) {
    data = data || {}
    _.extend(this, data)

    var m = moment(data.data_nascimento);
    this.data_nascimento = m.isValid() ? m : '';
}

Perfil.prototype.lattes_url = function() {
    if (!this.lattes)
        return "sem currículo Lattes";

    return "http://lattes.cnpq.br/" + this.lattes;
}

Perfil.prototype.add_fone = function(fone) {
    this.fones.push(fone);
}

Perfil.prototype.del_fone = function(index) {
    this.fones.splice(index, 1);
}

Perfil.prototype.del_email = function(index) {
    this.emails.splice(index, 1);
}

Perfil.prototype.add_email = function(email) {
    this.emails.push(email);
}

Perfil.prototype.del_vinculo = function(index) {
    if (this.vinculos[index].confirmed)
        return false;

    this.vinculos.splice(index, 1);
    return true;
}

Perfil.prototype.new_vinculo = function() {
    this.vinculos.push(new Vinculo());
}

function Vinculo(data) {
    data = data || {}
    this.projeto = data.projeto || '';
    this.funcao = data.funcao || '';
    this.inicio_at = data.inicio_at || moment(moment.now()).toISOString();
    this.fim_at = data.fim_at || null;
    this.sala = data.sala || '';
    this.state = data.state || 'new';
    this.confirmed = data.confirmed || false;
}
