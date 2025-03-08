# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, x):
    def retorna_resultado(y):
        return funcao(x,y)
    return retorna_resultado


# o numero passado soma com 5 sempre
soma_com_cinco = criar_funcao(soma, 5) 
# o numero passado multiplica com 5 sempre
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(4))
print(multiplica_por_dez(4))