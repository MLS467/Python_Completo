from Model.abstract_classe.Pessoa.Pessoa import Pessoa
from Model.abstract_classe.Contas.Conta import Conta

class Cliente(Pessoa):

    def __init__(self, nome, idade,conta:Conta):
        super().__init__(nome,idade)
        self.conta = conta

    def __str__(self):
        return f"Nome: {self.nome} - idade: {self.idade} -> saldo R${self.conta.saldo:.2f}"
    
    def abstract(self):...