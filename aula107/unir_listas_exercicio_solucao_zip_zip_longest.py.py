# # Exercício - Unir listas
# # Crie uma função zipper (como o zipper de roupas)
# # O trabalho dessa função será unir duas
# # listas na ordem.
# # Use todos os valores da menor lista.
# # Ex.:

# # ['Salvador', 'Ubatuba', 'Belo Horizonte']
# # ['BA', 'SP', 'MG', 'RJ']
# # Resultado
# # [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]


# def valida_lista(lista):
#     if not isinstance(lista, list):
#         raise TypeError("O tipo deve ser lista!")


# def zipper_decorador(func):
#     def zipper_aninhado(*args,**kwargs):
#         for arg in args:
#             try:
#                 valida_lista(arg)
#                 return func(*args,**kwargs)
#             except Exception as error:
#                 return f"Acabou a junção '{error}'"
#     return zipper_aninhado  


# @zipper_decorador
# def Zipper(lista1,lista2):
#     intervalo_maximo = min(len(lista1), len(lista2))
#     lista=[
#         (lista2[index],lista1[index])
#         for index in range(intervalo_maximo)
#     ]
#     return lista



estados = ['BA', 'SP', 'MG', 'RJ']
cidade = ['Salvador', 'Ubatuba', 'Belo Horizonte']


# print(Zipper('estados',cidade))

from itertools import zip_longest

# print(list(zip(cidade,estados)))
print(list(zip_longest(cidade,estados, fillvalue="SEM VALOR")))