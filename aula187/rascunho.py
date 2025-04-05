import sys


teste = sys.argv
qtd_args = len(teste)

if qtd_args <= 1:
    print("Você não passou argumentos")
else:
    print(f"Passou {qtd_args} argumentos")
