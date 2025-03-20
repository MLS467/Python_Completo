class Teste:
    def __init__(self,nome):
        self._nome = None
        self.nome = nome
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,nome):
        self._nome = nome


teste = Teste('teste')

print(teste.nome)