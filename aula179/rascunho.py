from pathlib import Path
import csv


CAMINHO_CSV = Path().absolute().parent / "Pesquisa_Satisfação.csv"

print(CAMINHO_CSV)

with open(CAMINHO_CSV, "r", encoding="utf-8") as arquivo_csv:
    # conteudo = csv.reader(arquivo_csv)
    conteudo = csv.DictReader(arquivo_csv)

    for linha in conteudo:
        print(linha["Endereço de e-mail"], linha["Qual a sua escolaridade?"])
