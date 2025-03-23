def my_repr(cls): 
     def new_repr(self):
       return f"Nome: {self.nome} classe: {self.__class__.__name__} "
     cls.__repr__ = new_repr # adiciona o repr dentro da classe
     return cls # retorna a classe 

@my_repr # decorador para adicionar o my_repr dentro da classe
class Time:

    def __init__(self, nome):
        self.nome = nome

@my_repr
class Planeta:

    def __init__(self, nome):
        self.nome = nome

   


brasil = Time('Brasil')
portugal = Time('Portugal')

print(brasil)
print(portugal)

terra = Planeta('Terra')
marte = Planeta('Marte')

print(terra)
print(marte)


