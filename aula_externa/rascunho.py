import pathlib

# import os
import shutil

caminho_projeto = pathlib.Path().absolute()
caminho_arquivo = pathlib.Path(__file__)

# print(caminho_arquivo)

# caminho_para_criar = caminho_projeto / 'text.txt'


# print(caminho_para_criar)


# home = os.path.expanduser('~')
# print(home)

# teste_home = pathlib.Path.home()
# caminho_novo_arq = caminho_projeto / 'teste.txt'
# caminho_novo_arq.touch()
# caminho_novo_arq.write_text("BATATA")


# print(caminho_novo_arq.read_text())
# caminho_novo_arq.unlink()

nova_pasta = caminho_projeto / "batata"
nova_pasta.mkdir(exist_ok=True)
sub_pasta = nova_pasta / "subpasta"
sub_pasta.mkdir(exist_ok=True)

mais_arquivo = sub_pasta / "text.txt"
mais_arquivo.touch()
mais_arquivo.write_text("Hey Bro")

# shutil.rmtree(nova_pasta)
