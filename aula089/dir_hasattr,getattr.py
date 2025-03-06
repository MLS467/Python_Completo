#dir, hasattr e getattr em python

string = "Maisson leal da silva"
metodo = 'lower'

if hasattr(string, metodo):
    print(f"Método {metodo} existe!")
    print(getattr(string,metodo)())
else:
    print(f"Método {metodo} não existe")