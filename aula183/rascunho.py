# import json
import locale
import pathlib
from datetime import datetime
import string


locale.setlocale(locale.LC_ALL, "")
CAMINHO_ARQUIVO = pathlib.Path(__file__).absolute().parent / "email.txt"


def formatar_valor_monetario(valor: float) -> str:
    valor_formatado = locale.currency(valor, True, True)
    return valor_formatado


pessoa = dict(
    nome="Maisson",
    valor=formatar_valor_monetario(1750),
    data=datetime.strftime(datetime(2025, 4, 1), "%d/%m/%Y"),
    empresa="MLS",
    telefone="53123456789",
)


texto = """Prezado(a) $nome,\n
Informamos que sua mensalidade será cobrada no valor de ${valor} no dia $data.
Caso deseje cancelar o serviço, entre em contato com a $empresa pelo telefone
$telefone.\n

Atenciosamentes,\n

${empresa},\n
"""


if not CAMINHO_ARQUIVO.exists():
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as arquivo:
        arquivo.writelines(texto)


if CAMINHO_ARQUIVO.exists():
    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo:
        arquivo_texto = arquivo.readlines()
        texto_str = str("".join(arquivo_texto))
        template = string.Template(texto_str)
        print(template.substitute(pessoa))
