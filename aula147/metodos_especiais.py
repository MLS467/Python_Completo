class PontoCar:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z


    def __repr__(self):
        return f"{self.__class__.__name__}(x={self.x!r},y={self.y!r},z={self.z!r})"


ponto = PontoCar(1,25,'str')
ponto2 = PontoCar(125,245,'String')

print(ponto)
print(ponto2)