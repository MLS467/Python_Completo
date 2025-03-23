from Model.abstract_classe.Contas.Conta import Conta
from Model.decoradores.Contas.sacar_conta_poupanca  import sacar_cp

class Conta_Poupanca(Conta):
    @sacar_cp
    def sacar(self, valor):
        self.saldo = self.saldo - valor
