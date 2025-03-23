from Model.exception.conta_corrente.ExceptionContas import MaiorZeroError 


def validar_maior_zero(func):
    def interna(self, valor):
        try:
            conta_atual = self.__class__.__name__ == 'Conta_Corrente'
            if not conta_atual:
                if valor <= 0:
                    raise MaiorZeroError("Valor igual ou menor que Zero!")
            
            if not isinstance(valor, (int,float)):
                raise TypeError("Valor inválido") 

            return func(self,valor)

        except MaiorZeroError as error:
            print(f"Erro ->", error)
        except TypeError as error:
            print(f"Erro ->", error)
        except Exception as error:
            print(f"Erro ->", error)

    return interna