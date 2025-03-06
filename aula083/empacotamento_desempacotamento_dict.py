pessoa = {
    "nome":"Maisson",
    "sobrenome":"Leal da Silva"
}

detalhes = {
    'idade':29,
    'altura':1.70
}

def mostra_dict(*args,**kwargs):
    print(args)
    for chave,valor in kwargs.items():
        print(f"{chave=} --> {valor=}")

# (chave_nome,nome),(chave_sobrenome,sobrenome) = pessoa.items()

# # print(chave_nome,nome)
# # print(chave_sobrenome,sobrenome)

# for chave,valor in pessoa.items():
#     print(chave, valor)

todos_dados = {**pessoa,**detalhes}

mostra_dict(1,2,3,valor=5,**todos_dados)
