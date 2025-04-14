import os
import shutil


HOME = os.path.expanduser("~")
DESKTOP = os.path.join(HOME, "Desktop")

CAMINHO_ORIGINAL = os.path.join(DESKTOP, "TESTE")
NOVA_PASTA = os.path.join(DESKTOP, "NOVA_PASTA")

os.makedirs(NOVA_PASTA, exist_ok=True)

# NÃO PRECISA ISSO
# if not os.path.exists(NOVA_PASTA):
#     os.makedirs(NOVA_PASTA)
#     print(f"{os.path.basename(NOVA_PASTA)} foi criada com sucesso!")

for root, dirs, files in os.walk(CAMINHO_ORIGINAL):
    for file in files:
        caminho_arquivo = os.path.join(CAMINHO_ORIGINAL, file)
        novo_caminho = os.path.join(NOVA_PASTA, file)
        print(caminho_arquivo)
        shutil.copy(caminho_arquivo, novo_caminho)
