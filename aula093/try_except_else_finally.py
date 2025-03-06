# try, except, else e finally

try:
    a = 18
    b = 0
    c = a / b
except NameError:
    print("Insira todos os dados")
except ZeroDivisionError as zero:
    print("Não pode ser dividido por zero!")
    print(zero.__class__.__name__)
except TypeError:
    print("Insira um numero do tipo correto")
except SyntaxError:
    print("Insira um numero")

