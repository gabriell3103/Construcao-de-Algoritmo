# 3. Escreva uma função recursiva que calcule a soma dos quadrados dos primeiros n números inteiros.

import unittest

def test_soma_quadrados_1():
    assert soma_quadrados(3) == 14
    print('OK - soma certo 01')

def test_soma_quadrados_2():
    assert soma_quadrados(0) == 1
    print('OK - soma certo 02')

def soma_quadrados(n):
    if n <= 1:
        return 1
    else:
        return n * n + soma_quadrados(n - 1)

n = int(input('Escreva um número: '))
resultado = soma_quadrados(n)
print("A soma dos quadrados dos primeiros", n, "números inteiros é", resultado)


if __name__ == '__main__':
    test_soma_quadrados_1()
    test_soma_quadrados_2()
    