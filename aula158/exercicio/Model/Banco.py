class Banco:
    def __init__(self, nome_banco,cliente):
        self._nome_banco = nome_banco
        self._agencias = [8,5,4,6,3]
        
        self._cliente = None
        self.cliente = cliente


    def autenticar(self):
        if self._nome_banco != self.cliente.conta.banco:
            return False
        elif not self.cliente.conta.agencia in self._agencias:
            return False
        return True
       
    def __repr__(self):
        return (f"Banco->{self._nome_banco}\n"
                f"Cliente -> {self.cliente}\n"
                f"Agência-> {self.cliente.conta.agencia}\n"
                f"Número_conta ->{self.cliente.conta.numero_conta}\n")

    @property
    def cliente(self):
        return self._cliente 
    
    @cliente.setter
    def cliente(self, valor):
            print('valida cliente')
            self._cliente = valor
