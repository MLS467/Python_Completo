"""
Cuidados com dados mutáveis

= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)

"""

lista_1 = ['Maisson','Luciane','Manuelle']
lista_2 = lista_1
lista_3 = lista_1.copy()
lista_1.append('X')

print(lista_1)
print(lista_3)