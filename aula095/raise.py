def nao_pode_ser_zero(n):
    if n == 0:
        raise ZeroDivisionError("O divisor não pode ser 'ZERO'")
    return True

def deve_ser_int_float(valor):
    if not isinstance(valor, (int,float)):
        raise TypeError(f'Tipo "{type(valor).__name__}" inválido')

def divide_numeros(dividendo,divisor):
    nao_pode_ser_zero(divisor)
    deve_ser_int_float(dividendo)
    deve_ser_int_float(divisor)
    return dividendo / divisor



print(divide_numeros(8,2))