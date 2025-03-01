# \n \r -> CRLF
#\n -> LF

#sep -> separador
#end -> break row (padrão) \n ou \r pode trocar por outro caracter

print(12,34, sep="-", end="##\n")
print(12,34, sep="-", end="\n\r")
print(56,78, sep=" ",end="\n")
print(9,10, sep=' ',end="\n")