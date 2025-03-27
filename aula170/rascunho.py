# C:\Users\lucia\Pictures

import os

caminho = os.path.join('C:\\Users', 'lucia', 'Pictures')

for item in os.listdir(caminho):
    novo_caminho = os.path.join(caminho, item)
    if os.path.isdir(novo_caminho):
        print('diretório ->', item)
    else:
        print('arquivo -> ', item)
