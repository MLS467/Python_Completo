class A:
    atributo_a = 'valor A'

    def metodo(self):
        print('A')


class B(A):
    atributo_b = 'valor B'

    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'valor C'

    def metodo(self):
        super(B, self).metodo()
        print('C')


teste = C()
print(C.mro())

print(teste.metodo())