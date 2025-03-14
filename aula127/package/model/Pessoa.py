class Pessoa:
    def __init__(self,nome,idade,altura,peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
    
    def pegar_dados(self):
        return vars(self)