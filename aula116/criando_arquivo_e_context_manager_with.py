# Criando arquivos com Python + Context Manager with
 # Usamos a função open para abrir
 # um arquivo em Python (ele pode ou não existir)
 # Modos:
 # r (leitura), w (escrita), x (para criação)
 # a (escreve ao final), b (binário)
 # t (modo texto), + (leitura e escrita)
 # Context manager - with (abre e fecha)
 # Métodos úteis
 # write, read (escrever e ler)
 # writelines (escrever várias linhas)
 # seek (move o cursor)
 # readline (ler linha)
 # readlines (ler linhas)
 # Vamos falar mais sobre o módulo os, mas:
 # os.remove ou unlink - apaga o arquivo
 # os.rename - troca o nome ou move o arquivo
 # Vamos falar mais sobre o módulo json, mas:
 # json.dump = Gera um arquivo json
 # json.load



caminho_arquivo = "C:\\Users\\lucia\\Documents\\curso_python\\arquivos"
caminho_arquivo += "\\texte.txt"
print(caminho_arquivo)




# arquivo = open(caminho_arquivo,'w')

# arquivo.close()

import os

lista = ['batata\n', 'feijão\n', 'arroz\n', 'leite\n', 'pao\n',('U+1F64F')]


with open(caminho_arquivo, 'w+', encoding="utf-8") as arquivo:
    arquivo.writelines(lista)
    arquivo.seek(0,0)
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())

# with open(caminho_arquivo, 'r') as arquivo:
    # print(arquivo.read())


# os.unlink(caminho_arquivo)