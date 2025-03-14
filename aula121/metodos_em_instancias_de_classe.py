class Carro:
    def __init__(self,nome):
        self.nome = nome
    
    def acelerar(self):
        print(f"{self.nome} Acelerou...")

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()