# EXERCÍCIO 7.5
# Reescreva o Programa 7.6 mas usando uma lista no lugar de um dicionário para armazenar valores intermediários.

import unittest

def test_fibonacci1():
    assert fib(0) == 0
    print('OK-1')
def test_fibonacci2():
    assert fib(1) == 1
    print('OK - 2')
def test_fibonacci3():   
    assert fib(8) == 21
    print('OK - 3')

def test_numeros_longos():
    assert fib(20) == 6765
    print('OK - 4')



fibonacci = [0, 1]

def fib(n: list) -> list:
    '''Calcula o n-ésimo termo da série de Fibonacci.'''
    if n >= len(fibonacci):
        for i in range(len(fibonacci), n + 1):
            fibonacci.append(fibonacci[i - 2] + fibonacci[i - 1])

    return fibonacci[n]


for i in range(100):
    print('fib ' + str(i) + ': ' + str(fib(i)))



if __name__ == '__main__':
    test_fibonacci1()
    test_fibonacci2()
    test_fibonacci3()
    test_numeros_longos()