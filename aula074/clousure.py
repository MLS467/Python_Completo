"""
Closure e funções que retornam outras funções
"""
import random


def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))



def criar_gerador_id():
    identificador = 0
    def valor():
        nonlocal identificador 
        identificador += 1
        ident = str(identificador) +'-'+ str(random.randint(1000,4000))
        return ident
    return valor

gera_id = criar_gerador_id()


print(gera_id())
print(gera_id())
print(gera_id())
print(gera_id())