"""
introdução ao desempacotamento + tuples (tuplas)
"""

lista = ['batata', 'arroz', 'feijão']

batata, *cereais = lista 

_,arroz,*_ = lista


print(arroz)