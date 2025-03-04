# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

import copy

pessoa = {
    'nome':'Maisson',
    'sobrenome':'Leal da Silva',
    'idade':29,
    'valores':[1,2,5,6,3,4,8]
}
 
# pes = copy.deepcopy(pessoa)
# pes['nome'] = 'batata'
# pes['valores'][0] = 'batata'

# print(id(pessoa))
# print(id(pes))
# print(pessoa)
# print(pes)


# print(pessoa['nome'])
# print(pessoa.get('nome') is None)

# valor_excluido = pessoa.pop('valores')
# print(valor_excluido)
# print(pessoa)

# ultima_chave = pessoa.popitem()
# print(ultima_chave)
# print(pessoa)


# pessoa.update({
#     'nome':'Barracuda',
#     'R$': 500
#     })

pessoa.update(nome="Barbaridade", idade='51')

# tupla = (('nome', 'novo_valor'),('idade',1500))
lista = [['nome', 'novo_valor'],['idade',1500]]

pessoa.update(lista)

print(pessoa)