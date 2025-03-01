"""
introdução ao try/except
try -> tenta executar o código
except -> ocorreu algum erro ao tentar executar

"""

numero = input("Vou dobrar o número que vc digitar: ")

try:
    print('chegou aqui')
    print(numero**2)
    print('chegou aqui depois do erro')
except:
    print('Não é um número!')


# if numero.isdigit():
#     ...
# else:
#     print('Não é um número!')