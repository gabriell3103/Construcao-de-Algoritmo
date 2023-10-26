# Teste Unitário
# Renomeie o nome do arquivo para main para funcionar

import unittest

def soma(a, b):
    return a + b

# def soma(a, b):
#     return a * b

def test_soma():
    assert soma(1, 2) == 3
    print('Ok - Soma')

def quadrado(a):
    return a**2

def test_quadrado():
    assert quadrado(4) == 16
    print('Ok - Quadrado')

def par_ou_impar(n):
    return 'impar' if n % 2 != 0 else 'par'

def test_num_par():
    assert par_ou_impar(2) == 'par'
    print('OK - Par')

def test_num_impar():
    assert par_ou_impar(3) == 'impar'
    print('OK - Impar')
    

if __name__ == '__main__':
    test_soma()
    test_quadrado()
    test_num_par()
    test_num_impar()