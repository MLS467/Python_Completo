def fabrica_de_funcoes(func):
    print("Decoradora 1")

    def aninhada(*args,**kwargs):
        print("Aninhada")
        return func(*args,**kwargs)
    return aninhada


 
@fabrica_de_funcoes
def soma(x,y):
    return x +y

print(soma(5,6))
print(soma(5,8))