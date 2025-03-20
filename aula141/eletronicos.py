from log import LogFileMixin

class Eletronicos:
    def __init__(self,nome):
        self._nome = nome
        self._ligado = False
    
    def ligar(self):
        if not self._ligado:
            self._ligado = True

    def desligar(self):
        if self._ligado:
            self._ligado = False


class SmartPhone(Eletronicos,LogFileMixin):
    
    def ligar(self):
        super().ligar()
        self._logs("Ligou agora")
        self.log_success("Bolado")

    def desligar(self):
        self._logs("Desligou agora")
        self.log_error("Não Bolado")
        super().desligar()


if __name__ == '__main__':
    galaxy_x = SmartPhone('LG444')
    galaxy_x.ligar()
    galaxy_x.desligar()

    print(vars(galaxy_x))