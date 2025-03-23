from abc import ABC, abstractmethod
from Model.decoradores.Contas.maior_zero_decorador import \
    validar_maior_zero

class Conta(ABC):
    def __init__(self, valor, numero_conta,banco,agencia):
        self.numero_conta = numero_conta
        self.agencia = agencia
        self.banco = banco
        self._saldo = None
        self.saldo = valor

    @abstractmethod
    def sacar(self,valor): ...

    @validar_maior_zero
    def depositar(self,valor):
        self.saldo += valor

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    @validar_maior_zero
    def saldo(self,valor):
        self._saldo = valor

    def __str__(self):
        try:
            return f"{self.__class__.__name__} - {f"R${self.saldo:.2f}"}"
        except TypeError as error:
            return f"{self.__class__.__name__} - {f"R${self.saldo}"}"
