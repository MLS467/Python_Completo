import enum

direcoes = enum.Enum('Dir', ['ESQUERDA', 'DIREITA', 'CIMA', 'BAIXO'])

def teste_direcoes(direcao:direcoes):
    if not isinstance(direcao, direcoes):
        raise TypeError("Tipo inválido")
    
    return f"direcao: {direcao.name} - valor: {direcao.value}"


teste = teste_direcoes(direcoes.CIMA)
print(teste)