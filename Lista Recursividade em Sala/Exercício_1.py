# 1. Escreva uma função recursiva para calcular o fatorial de um número n.

import unittest

def test_fatorial_1():
    assert fatorial(4) == 24

def test_fatorial_5():
    assert fatorial(5) == 120

def test_fatorial_0():
    assert fatorial(0) == 0

def fatorial(n):
    if n <= 1:
        return n
    else:
        return n * fatorial(n - 1)
    

num = int(input('Escreva um número: '))
fat = fatorial(num)
print(fat)

if __name__ == '__main__':
    test_fatorial_1()
    print('1 - Funciona')
    test_fatorial_5()
    print('5 - Funciona')
    test_fatorial_0()
    print('0 - Funciona')
