"""
for in com listas
"""

lista = [ 'Maria','Helena', 'Luiz', 'Tereza']
lista.append('Rodrigo')

indices = range(len(lista))

for indice in indices:
    print(indice ,lista[indice], type(lista[indice]))