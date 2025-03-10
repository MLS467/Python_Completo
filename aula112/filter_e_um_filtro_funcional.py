
produtos = [
     {'nome': 'Produto 5', 'preco': 10.00},
     {'nome': 'Produto 1', 'preco': 22.32},
     {'nome': 'Produto 3', 'preco': 10.11},
     {'nome': 'Produto 2', 'preco': 105.87},
     {'nome': 'Produto 4', 'preco': 69.90},
 ]

nova_lista1 = [
    produto
    for produto in produtos
    if produto['preco'] > 15
]


nova_lista2 = list(filter(
    lambda produto:produto['preco'] > 15,
    produtos
))

print(*nova_lista1, sep='\n')
print()
print(*nova_lista2, sep='\n')