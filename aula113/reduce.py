import functools

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

total = functools.reduce(
    lambda acum,prod: acum + prod['preco'],
    produtos,
    0
)
print(round(total, 2))

# lista = [
#     produto['preco']
#     for produto in produtos
# ]

# print(round(sum(lista),2))