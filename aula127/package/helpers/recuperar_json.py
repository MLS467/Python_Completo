import json

def recuperar_json():
    caminho_total = "C:\\Users\\lucia\\Documents\\curso_python\\aula127\\package\\db\\"
    arquivo = caminho_total + "pessoa.json"

    with open(arquivo,'r',encoding='utf-8') as arquivo_atual:
        dados = json.load(arquivo_atual)
        return dados