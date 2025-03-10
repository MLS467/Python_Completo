import pymysql

# def fatorial(n):
#     acum = 1
#     for i in range(n,0,-1):
#         acum *= i
#     return acum

def fatorial(n):

    if n == 1:
        return 1
    
    resultado = n * fatorial(n-1)
    return resultado



print(fatorial(5))