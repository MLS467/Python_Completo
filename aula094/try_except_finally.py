# try, except, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
try:
    print("Abriu arquivo")
    a = 18
    b = '1'
    c = a / b
except ZeroDivisionError as error_zero:
    print("Dividiu por zero", f"({error_zero})")
except NameError as name_error:
    print("Sem valor atribuido",f"({name_error})")
except TypeError as error_tipo:
    print("Tipo está não é válido", f"({error_tipo})")
except Exception:
    print("Erro desconhecido!")
else: # executa quando o try passa sem erro
    print("Executou sem erro")
finally: # sempre é executado independente do resultado
    print("Fechar arquivo")
