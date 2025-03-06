

def generator(n=0):
    print("Iniciando gerador")
    yield 1 
    print('Acabou')
    yield 2


valor = generator(n=0) # cria o gerador

print(next(valor)) # primeira chamada para no primeiro yield
# print(next(valor)) # segunda chamada para no segundo yield