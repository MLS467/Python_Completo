def valor_maior_que_zero(valor):
    if valor <= 0:
        raise ValueError("Valor deve ser maior que Zero")
    return True

def valor_numerico(valor):
    if not isinstance(valor, (int,float)):
        raise TypeError("O valor deve ser um número")
    return True

def validar(valor):
    valor_numerico(valor)
    valor_maior_que_zero(valor)

def desconto(percentual):
    try:
        validar(percentual)
        desconto_percentual = (100 - percentual) / 100

        def desconto_sobre_valor(valor):
            try:
                validar(valor)
                nonlocal desconto_percentual
                return f"desconto de {percentual}%, total é de R${valor * desconto_percentual:.2f} reais" 
            except Exception as e:
                return e
            
    except Exception as e:
        return e
    
    return desconto_sobre_valor


desconto_janeiro = desconto(10)


print(desconto_janeiro(0))