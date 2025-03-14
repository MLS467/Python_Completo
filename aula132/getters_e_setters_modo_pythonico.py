class Caneta:
    def __init__(self,cor):
        self._cor = cor

    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self,valor):
        if valor.lower() == "vermelha":
            raise ValueError("Não pode vermelha")
        self._cor = valor

caneta_cor = Caneta("Azul")

print(caneta_cor.cor)
print(caneta_cor.cor)
caneta_cor.cor = "verde"
print(caneta_cor.cor)
print(caneta_cor.cor)
print(caneta_cor.cor)

