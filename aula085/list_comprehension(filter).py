import pprint

def p(valor):
    pprint.pprint(valor, sort_dicts=False)


produtos = [
    {"nome":"batata", 'preco': 10},
    {"nome":"feijão", 'preco': 15},
    {"nome":"carne", 'preco': 20}
]


# lista = [
#     n for n in range(10)
#     if n > 4
#     ]

# p(lista)


lista_filtrada = [
    # Mapeamento
    {**produto,'preco':produto['preco'] * 1.05} if \
    produto['preco'] > 12 else {**produto}

    for produto in produtos

    # Filtro
    if produto['preco'] > 10
 ]

p(lista_filtrada)