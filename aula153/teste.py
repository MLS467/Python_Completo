class CallMe:
    def __init__(self,number):
        self.number = number

    def __call__(self, *args, **kwargs):
        print(f"nome: {kwargs['nome']} e numero {self.number}")


c1 = CallMe('123123')

c1(nome='Maisson')