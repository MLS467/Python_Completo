"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
# lista.append(50)
# lista.pop()
# lista.append(60)
# lista.append(70)
# ultimo_valor = lista.pop(3)
# print(lista, 'Removido,', ultimo_valor)



lista = [1,2,5,6,9,5,4,22,5,6,5,14,2,335,5]


index_valor = lista.index(335)
valor_excluido = lista.pop(index_valor)
lista.append(555)

print(lista,valor_excluido)
