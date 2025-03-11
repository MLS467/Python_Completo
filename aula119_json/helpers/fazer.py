import os
import json
import random

caminho_db = "C:\\Users\\lucia\\Documents\\curso_python\\aula119_json\\helpers\\db\\"
novo_arquivo = caminho_db+"db.json"

def adicionar_nova_tarefa(tarefa):
    arquivos = os.listdir(caminho_db)
    dados = []
    if 'db.json' in arquivos:
        with open(novo_arquivo,"r",encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    dados.append({'id':random.randint(1000,9999),'tarefa':tarefa})
    with open(novo_arquivo,"w",encoding="utf-8") as arquivo:
        json.dump(dados,arquivo, ensure_ascii=True,indent=2)