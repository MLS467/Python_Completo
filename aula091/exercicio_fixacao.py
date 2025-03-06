valor_a = (_*2 for _ in range(1000))

def gerar_bloco(valor):
    count = 10
    lista = []
    for val in valor:
        lista.append(val)
        count -= 1
        if not count:
            yield lista
            count = 10
            lista = []



gerador_lista = gerar_bloco(valor_a)

valor = next(gerador_lista)
print(valor)
print(next(gerador_lista))
print(next(gerador_lista))