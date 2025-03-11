import copy
import json

def listar():
  caminho_db = "C:\\Users\\lucia\\Documents\\curso_python\\aula119_json\\helpers\\db\\"
  novo_arquivo = caminho_db+"db.json"
  with open(novo_arquivo,'r',encoding="utf-8") as arquivo:
    dados = json.load(arquivo)
    dados_copy = copy.deepcopy(dados)
    for valor in dados_copy:
      print(f"{valor['id']} --> {valor['tarefa']}")

