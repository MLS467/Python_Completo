import json
import os

def salvar_json(dados_json):
    caminho_total = "C:\\Users\\lucia\\Documents\\curso_python\\aula127\\package\\db\\"
    arquivo = caminho_total + "pessoa.json"
    lista_de_diretorios = os.listdir(caminho_total)

    dados = []
    if 'pessoa.json' in lista_de_diretorios:
        with open(arquivo,'r',encoding='utf-8') as arquivo_atual:
            dados = json.load(arquivo_atual)
    dados.append(dados_json)
    
    with open(arquivo,'w',encoding='utf-8') as novo_arquivo:
        json.dump(
            dados,
            novo_arquivo,
            ensure_ascii=False,
            indent=2
            )



