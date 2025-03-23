from Model.exception.conta_corrente.ExceptionContas import ValorInvalidoError
from Model.exception.conta_corrente.ExceptionContas import MaiorZeroError

def sacar_cc(func):
    def interna(self,valor):
        try:
            if not isinstance(valor, (int, float)):
                raise ValueError("Valor inválido") 

            if valor <= 0:
                raise MaiorZeroError("Valor igual ou menor que Zero!")

            valor_restante = self.saldo - valor < -100
            if valor_restante:
                raise ValorInvalidoError("Permitido saldo negativo até R$-100,00")

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