# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

import sys

import aula097_m as teste5
from teste import teste
from teste.teste import chamou


# sys.path.append('C:/Users/lucia/Documents/curso_python/teste')

# import teste 

print('Esse módulo se chama -->', __name__)

chamou()

teste5.chamar()