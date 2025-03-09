def valida_lista(lista):
    if not isinstance(lista, list):
        raise TypeError("O tipo deve ser lista!")

def decorador_soma(func):
    def soma_aninhada(*args,**kwargs):
        try:
            valida_lista(args[0])
            valida_lista(args[1])
            resultado = func(*args,**kwargs)
            return resultado
        except Exception as error:
            print(error)
    return soma_aninhada
