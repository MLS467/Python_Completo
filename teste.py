def soma(x,y):
    return x + y

def exibe(cont,res):
    return f"Função chamada {cont} vezes  -> Retorna {res}"

def cria_funcao(func):
    contador = 0
    def funcao_interna(*args):
        nonlocal contador
        contador += 1
        resultado = func(*args)
        return [contador,resultado]
    return funcao_interna


func_criada = cria_funcao(soma)

print(exibe(*func_criada(1,2)))
print(exibe(*func_criada(5,7)))
