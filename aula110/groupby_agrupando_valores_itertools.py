import itertools

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]


teste = ['a','a','a','b','b','c','c','a']

# print(list(itertools.groupby(teste)))

ordenar_por = lambda i:i['nota']

nova_lista = sorted(alunos, key=ordenar_por)
for chave,valor in itertools.groupby(nova_lista,key=ordenar_por):
    print(chave)
    for i in list(valor):
        print(i)