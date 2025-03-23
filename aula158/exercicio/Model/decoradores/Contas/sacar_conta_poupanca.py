from Model.exception.conta_corrente.ExceptionContas import ValorInvalidoError
from Model.exception.conta_corrente.ExceptionContas import MaiorZeroError

def sacar_cp(func):
    def interna(self,valor):
        try:
            if not isinstance(valor, (int, float)):
                raise ValueError("Valor inválido") 

            if valor <= 0:
                raise MaiorZeroError("Valor igual ou menor que Zero!")

            valor_restante = self.saldo - valor < 0
            if valor_restante:
                raise ValorInvalidoError("Saldo insufiente para o saque")

            return func(self,valor)
        
        except MaiorZeroError as error:
            print(f"Erro ->", error)
        except ValueError as error:
            print(f"Erro ->", error)
        except ValorInvalidoError as error:
            print(f"Erro ->", error)
        except Exception as error:
            print(f"Erro ->", error)

    return interna
