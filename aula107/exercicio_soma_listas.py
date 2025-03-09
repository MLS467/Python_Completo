from decorador import decorador_soma

def pegar_lista_menor(lista1,lista2):
    tam_lista_menor = min(len(lista1),len(lista2))
    return tam_lista_menor

@decorador_soma
def soma_listas(lista1,lista2):
    tamanho_max = pegar_lista_menor(lista1,lista2)

    lista_somados = [
        lista1[i] + lista2[i]
        for i in range(tamanho_max)
    ]

    return lista_somados



lista1 = list(range(0,50,2))
lista2 = list(range(0,50,3))


print(lista1)
print(lista2)
print(soma_listas(lista1,lista2))


