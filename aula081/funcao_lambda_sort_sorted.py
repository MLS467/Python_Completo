# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]
# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort(reverse=True)
# sorted(lista)
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# lista = [1,2,22,77,8,7,9]
# lista.sort(reverse=True)


# nova_lista = sorted(lista)

# print(lista)


# print(nova_lista)

# def ordenador(valor):
#     return valor['sobrenome']

# lista.sort(key=ordenador)

# lista.sort(key=lambda item: item['nome'])

def exibir(lista):
    for i in lista:
        print(i)
    print()

lista_por_nome = sorted(lista, key=lambda item:item['nome'])
lista_por_sobrenome = sorted(lista, key=lambda item:item['sobrenome'])


exibir(lista_por_nome)
exibir(lista_por_sobrenome)
