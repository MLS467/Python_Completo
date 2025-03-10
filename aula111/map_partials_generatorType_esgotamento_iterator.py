import functools 
import itertools

produtos = [
     {'nome': 'Produto 5', 'preco': 10.00},
     {'nome': 'Produto 1', 'preco': 22.32},
     {'nome': 'Produto 3', 'preco': 10.11},
     {'nome': 'Produto 2', 'preco': 105.87},
     {'nome': 'Produto 4', 'preco': 69.90},
 ]

def exibir(valor):
    print(*valor, sep="\n")


def aumentar_porcentagem(valor,porcentagem):
    return round(valor * porcentagem, 2)


aumentar_por_cento = functools.partial(
    aumentar_porcentagem,
    1.1
)

lista_nova = [
        {**produto, 'preco':aumentar_por_cento(produto['preco'])}
        for produto in produtos
    ] 

# lista_nova = list(map(
#     lambda x : x * 3,
#     [1,2,3]
# ))


exibir(produtos)
print()
exibir(lista_nova)
