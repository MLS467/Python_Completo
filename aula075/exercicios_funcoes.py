def multiplicar(vezes):
    def valor_multiplicado(valor):
        return vezes * valor
    return valor_multiplicado


duplicar = multiplicar(2)
triplicar = multiplicar(3)
quadruplicar = multiplicar(4)


print(duplicar(2))
print(triplicar(5))
print(quadruplicar(4))