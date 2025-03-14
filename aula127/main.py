from package import Pessoa, salvar_json, recuperar_json


pessoa1 = Pessoa("Maisson",29,1.7,85.5)
pessoa2 = Pessoa("Luciane",32,1.56,75.5)
dados_json = pessoa1.pegar_dados()
dados_json2 = pessoa2.pegar_dados()

# salvar_json(dados_json)
# salvar_json(dados_json2)

recuperados = recuperar_json()

pessoa3 = Pessoa(**recuperados[0])

print(pessoa3.nome)
print(pessoa3.altura)
