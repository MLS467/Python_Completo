"""
Intordução às funções (def) em Python
Funções são como trechos de códigos usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funçoes Python retornam None (nada)
"""

def cotacao(real,dolar):
    print(f"R${real:,.2f} real(is) em dolar são = ${real / dolar:,.2f} dolar(es)")


def saudacao(nome):
    print(f"Olá, {nome}")

saudacao('Maisson')
saudacao('Luciane')

cotacao(1000000,5.9)