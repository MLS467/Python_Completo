"""
Documentando funções com Docstrings

- Docstrings são strings de documentação
- Utilizamos aspas triplas para definir um docstring
- Podemos acessar a documentação de uma função em Python utilizando a 
propriedade especial __doc__

"""

variavel_1 = 1


def soma(x:int | float, y:int | float) -> int | float:
    """Soma x e y

    :param x: Primeiro número
    :param y: Segundo número
    :return: A soma entre x e y
    
    """
    return x + y