# Manipulando chaves e valores em dicionários

# pessoa = {
#     'nome':'Luiz Otávio',
#     'sobrenome':'Miranda',
#     'idade':18,
#     'altura':1.8,
#     'endereco': [
#         {'rua':'tal tal', 'numero':123},
#         {'rua':'outra tal', 'numero':321},
#     ],
# }


pessoa={}

chave = 'nome'

pessoa[chave] = 'Maisson'
pessoa['sobrenome']="Leal da Silva"

# del pessoa['sobrenome']

print(pessoa)
print(pessoa[chave])

if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(f"Existe e o valor é {pessoa.get('sobrenome')} ")