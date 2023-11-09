# EXERCÍCIO 7.4
# Escreva uma função que calcule o fatorial de um número. O fatorial pode ser definido como:
#         {    1,     se n é 0
# fat(n) -
#         { n x fat(n-1),  se n é maior que 0

import unittest

def test_fatorial1():
    assert calcular_fatorial(4) == 24
    print('OK - 1')
def test_fatorial2():
    assert calcular_fatorial(0) == 1
    print('OK - 2')


def calcular_fatorial(num: int):
    if num == 0:
        return 1
    elif num > 0:
        return num * calcular_fatorial(num - 1)

    return "Fatorial indefinido para números negativos"


n = 5
resultado = calcular_fatorial(n)
print(f'O fatorial de {n} é {resultado}')

if __name__ == '__main__':
    test_fatorial1()
    test_fatorial2()