import csv
import pathlib

usuarios = [
    {
        "nome": "Lucas",
        "idade": 25,
    },
    {
        "nome": "Ana",
        "idade": 22,
    },
    {
        "nome": "Carlos",
        "idade": 30,
    },
    {
        "nome": "Maria",
        "idade": 28,
    },
    {
        "nome": "João",
        "idade": 35,
    },
    {
        "nome": "Fernanda",
        "idade": 27,
    },
    {
        "nome": "Pedro",
        "idade": 29,
    },
    {
        "nome": "Juliana",
        "idade": 24,
    },
    {
        "nome": "Ricardo",
        "idade": 31,
    },
    {
        "nome": "Tatiane",
        "idade": 26,
    }
]


CAMINHO_PASTA = pathlib.Path(__file__).parent.resolve() / 'usuarios.csv'

with open(CAMINHO_PASTA, 'w', encoding='utf-8') as arquivo:
    resultado = usuarios[0].keys()
    escritor = csv.writer(arquivo)

    escritor.writerow(resultado)

    for usuario in usuarios:
        escritor.writerow(usuario.values())
