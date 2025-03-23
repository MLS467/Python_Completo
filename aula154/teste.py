class Multiplicar:
    def __init__(self, func):
       self.func = func
    
    def __call__(self, *args, **kwds):
        print(args, kwds) 
        return self.func(*args, **kwds)


def dec_func_multi(func):
    def nested_multi(*args,**kwargs):
        # validações e testes 
        # se passar executa
        return func(*args,**kwargs)
    return nested_multi



@Multiplicar
def multi(*args, **kwds):
    acum = 1
    for i in args:
        acum*= i
    return acum


print(multi(2,2,2,66))