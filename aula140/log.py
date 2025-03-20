class Log:

    def logs(self,msg):
        raise NotImplementedError("Método não implementado")
    


class LogFileMixin(Log):
  def logs(self,msg):
      print(msg)

if __name__ == '__main__':
    l1 = Log()
    l1.logs('batata')
