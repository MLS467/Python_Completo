import pathlib
import subprocess

# Caminho para o arquivo .txt
PATH_FILE = pathlib.Path(__file__).parent / "ordem_das_aulas_por_commit.txt"

# Lê a última linha do arquivo
with open(PATH_FILE, "r", encoding="utf-8") as f:
    linhas = f.readlines()
    if not linhas:
        print("O arquivo está vazio.")
        exit()
    ultima_linha = linhas[-1].strip()

# Adiciona mudanças ao Git
# Faz o commit com a última linha como mensagem
subprocess.run(["git", "c", ultima_linha])
