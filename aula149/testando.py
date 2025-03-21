from pathlib import Path

PATH_FOLDER = Path(__file__).parent / 'teste.txt'

class MyOpen():
    def __init__(self,caminho,modo):
        self.caminho = caminho
        self.modo = modo
        self.arquivo = None

    def __enter__(self):
      self.arquivo = open(self.caminho,self.modo, encoding='utf-8')
      return self.arquivo  
    
    def __exit__(self, class_exception, exception, traceback):
        print("Olá Exit")
        self.arquivo.close()
        return True # Tratei a exceção


with MyOpen(PATH_FOLDER,'w') as teste:
    teste.write("Batata\n",123)
    teste.write("Feijao\n")

