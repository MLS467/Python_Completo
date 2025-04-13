import pathlib

NOME_ARQUIVO_ATUAL = input("Digite o nome do arquivo atual: ")
PASTA_ORIGINAL = input("Digite o nome da pasta original: ")


def criar_pasta_da_aula(nome_pasta: str, nome_arquivo: str) -> None:
    CAMINHO_RAIZ = pathlib.Path(__file__).parent / nome_pasta
    CAMINHO_NOVA_PASTA = CAMINHO_RAIZ / f"{nome_arquivo.replace(" ", "_")}.py"
    CAMINHO_RASCUNHO = CAMINHO_RAIZ / "rascunho.py"

    LISTA_ARQUIVOS = [CAMINHO_NOVA_PASTA, CAMINHO_RASCUNHO]

    CAMINHO_RAIZ.mkdir(exist_ok=True)

    for arquivo in LISTA_ARQUIVOS:
        arquivo.touch(exist_ok=True)


criar_pasta_da_aula(PASTA_ORIGINAL, NOME_ARQUIVO_ATUAL)
