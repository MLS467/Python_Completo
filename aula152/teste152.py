def retorna_nome(metodo):
    def r_nome(self, *args, **kwargs):
        print("ENTROU")
        return metodo(self, *args, **kwargs)
    return r_nome


def retorna_repr(self):
    return f"Nome {self.__class__.__name__} {self.nome}"


def my_repr(cls):
    cls.__repr__ = retorna_repr
    return cls



@my_repr
class Time:
    def __init__(self, nome):
        self.nome = nome

@my_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    @retorna_nome
    def fala_nome(self):
        return f"nome -> {self.nome}"




brasil = Time('Brasil')
portugal = Time('Portugal')
japao = Time('Japão')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)
print(japao)

print(terra.fala_nome())
print(marte)