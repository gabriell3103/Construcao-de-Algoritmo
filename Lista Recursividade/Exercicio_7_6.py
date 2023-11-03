# EXERCÍCIO 7.6
# Escreva uma função recursiva que some os n primeiros números.

import unittest

def test_soma1():
    assert soma_n_primeiros_numeros(4) == 10
    print('OK - 1')
def test_soma2():
    assert soma_n_primeiros_numeros(1) == 1
    print('OK - 2')

def test_soma3():
    assert soma_n_primeiros_numeros(0) == 'Apenas numeros maiores que 0'
    print('OK - 3')

def soma_n_primeiros_numeros(n: int):
    if n < 1:
        return 'Apenas numeros maiores que 0'
    elif n == 1:
        return 1
    else:
        return n + soma_n_primeiros_numeros(n - 1)


n = 5
resultado = soma_n_primeiros_numeros(n)
print(f'A soma dos primeiros {n} números é {resultado}')


if __name__ == '__main__':
    test_soma1()
    test_soma2()
    test_soma3()