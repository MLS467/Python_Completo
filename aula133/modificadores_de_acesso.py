class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None
    
    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self,ferramenta):
        self._ferramenta = ferramenta

    def mostrar(self):
        print(f"O Escritor {self.nome} está escrevendo com uma {self.ferramenta.ferramenta} !")


class Ferramenta:
    def __init__(self, ferramenta):
        self.ferramenta = ferramenta

    def escrevendo(self):
        print(f"Escrevendo com uma {self.ferramenta}")


escritor = Escritor('Maisson')
ferramenta = Ferramenta('Maquina de escrever')
escritor.ferramenta = ferramenta
escritor.ferramenta.escrevendo()

print(escritor.mostrar())