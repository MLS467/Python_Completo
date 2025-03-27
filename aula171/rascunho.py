import os
# C:\Users\lucia\Desktop
caminho = caminho = os.path.join('C:\\Users', 'lucia', 'Desktop', 'teste')

for root, dirs, arquivo in os.walk(caminho):
    print('raiz -> ', root)

    for pastas in dirs:
        print('subpastas -> ', pastas)
    for arq in arquivo:
        print('arquivo -> ', arq)
        os.unlink(os.path.join(root, arq))
