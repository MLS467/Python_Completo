import os

# C:\Users\lucia\Desktop\teste
caminho = os.path.join("C:\\Users\\lucia", "Desktop", "teste", "arquivo.txt")


# print(caminho)
caminho_dir, arquivo = os.path.split(caminho)  # faz o caminho do arquivo
# print(arquivo)

nome_arq, extensao_arq = os.path.splitext(arquivo)  # Separa nome e extensão

# print(nome_arq, extensao_arq)


existe = os.path.exists(caminho)  # testa se existe ou não

# print(existe)
absoluto = os.path.abspath(".")  # mostra o caminho com path absoluto

# print(absoluto)

basenome = os.path.basename(caminho)  # pega o final do caminho

# print(basenome)

dirname_ = os.path.dirname(caminho)  # pega todos diretórios do caminho

print(dirname_)
