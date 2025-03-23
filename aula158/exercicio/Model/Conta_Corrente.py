from Model.abstract_classe.Contas.Conta import Conta
from Model.decoradores.Contas.sacar_conta_corrente import sacar_cc

class Conta_Corrente(Conta):
    @sacar_cc
    def sacar(self, valor):
        self.saldo = self.saldo - valor

