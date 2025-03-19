# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Fabricante:
    def __init__(self,nome):
        self.nome = nome
        self.carros = []

    def inserir_carro(self,carro):
        self.carros.append(carro)
    
    def mostrar_carro(self):
        for index,carro in enumerate(self.carros):
            print(f'{f" {index +1 } Carro ":*^50}')
            print(f"Carro : {carro.nome}")
            print(f"Fabricante: {self.nome}")
            print(f"Motor: {carro.motor.nome}")
            print('*'*50)

class Motor:
    def __init__(self,nome):
        self.nome = nome

class Carro:
    def __init__(self,nome):
        self.nome = nome
        self._motor = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self,valor):
        self._motor = valor

fabricante = Fabricante('Volkswage')

motor = Motor("V8")
carro = Carro('Fusca')

carro2 = Carro("Brasilia")
carro2.motor = motor

carro.motor = motor

fabricante.inserir_carro(carro)
fabricante.inserir_carro(carro2)
fabricante.mostrar_carro()


