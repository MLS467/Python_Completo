import json
import os
import pprint


def iniciar_arquivo(caminho, conteudo):
    with open(caminho, "w", encoding="UTF-8") as arquivo:
        json.dump(conteudo, arquivo, ensure_ascii=False, indent=2)


def ler_arquivo(caminho):
    with open(caminho, "r", encoding="UTF-8") as arquivo:
        json_ler = json.load(arquivo)
    pprint.pprint(json_ler)


NOME_ARQUIVO = "aula177.json"
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(".")
CAMINHO_DIR = os.path.dirname(__file__)
CAMINHO_FINAL = os.path.join(
    CAMINHO_ABSOLUTO_ARQUIVO, CAMINHO_DIR, NOME_ARQUIVO
)

string_json = {
    "title": "O Senhor dos Anéis: A Sociedade do Anel",
    "original_title": "The Lord of the Rings: The Fellowship of the Ring",
    "is_movie": True,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
    "budget": None,
}


iniciar_arquivo(CAMINHO_FINAL, string_json)

ler_arquivo(CAMINHO_FINAL)
