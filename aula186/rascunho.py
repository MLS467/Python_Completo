import os
import pathlib
import zipfile


# cria uma pasta com arquivos para simular
def criar_pasta(qtd: int, path: pathlib.Path):
    for i in range(1, qtd + 1):
        texto = f"text{i}.txt"
        with open(os.path.join(path, texto), "w", encoding="utf-8") as arquivo:
            arquivo.write(texto)


# compactar pasta com o caminho da pasta e o caminho da pasta .zip
def compacta_pasta(old_path: pathlib.Path, new_path_zip: pathlib.Path):
    with zipfile.ZipFile(new_path_zip, "w") as zip:
        for root, dirs, files in os.walk(old_path):
            for file in files:
                zip.write(os.path.join(root, file), file)


# ler arquivos das pastas compactada
def ler_pasta_compacta(path: pathlib.Path):
    with zipfile.ZipFile(path, "r") as arquivos:
        arquivos_sorted = sorted(arquivos.namelist())
        for arq in arquivos_sorted:
            print(arq)


# caminhos para exercitar
CAMINHO_ROOT = pathlib.Path(__file__).absolute().parent
CAMINHO_PASTA_DIR = CAMINHO_ROOT / "TESTE_ZIP"
CAMINHO_PASTA_ZIP = CAMINHO_ROOT / "PASTA.zip"
CAMINHO_PASTA_DIR.mkdir(exist_ok=True)

# chamada das funções
# criar_pasta(10, CAMINHO_PASTA_DIR)
# compacta_pasta(CAMINHO_PASTA_DIR, CAMINHO_PASTA_ZIP)
ler_pasta_compacta(CAMINHO_PASTA_ZIP)
