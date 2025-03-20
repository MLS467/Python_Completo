from pathlib import Path

LOG_PATH = Path(__file__).parent / 'log/text.txt'

class Log:
    def _logs(self,msg):
        raise NotImplementedError("Método não implementado")
    
    def log_error(self,msg):
        print(f"Erro {msg}")

    def log_success(self,msg):
        print(f"Sucesso {msg}")

class LogFileMixin(Log):
  
  def _logs(self,msg):
        with open(LOG_PATH, 'a',encoding='utf-8') as arquivo:
            arquivo.write(msg)
            arquivo.write('\n')

if __name__ == '__main__':
    l1 = LogFileMixin()
    l1._logs('feijao')
