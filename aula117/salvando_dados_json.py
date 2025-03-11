pessoa = {
"nome": "Luiz Otávio 2",
"sobrenome": "Miranda",
"enderecos": [
    {
    "rua": "R1",
    "numero": 32
    },
    {
    "rua": "R2",
    "numero": 55
    }
],
"altura": 1.8,
"numeros_preferidos": (
    2,
    4,
    6,
    8,
    10
),
"dev": True,
"nada": None
}

import json

caminho_pasta = "C:\\Users\\lucia\\Documents\\curso_python\\aprendendo_json\\"

arquivo = caminho_pasta + "pessoa.json"

# with open(arquivo, 'w', encoding='utf-8') as novo_arquivo:
#     json.dump(
#         pessoa, #dicionário 
#         novo_arquivo, # arquivo criado
#         ensure_ascii=True,
#         indent=2
#         )

with open(arquivo, 'r', encoding='utf-8') as arq: 
    pes = json.load(arq)
    print(pes)