# 2. Escreva uma função recursiva que calcule a soma dos dígitos de um número inteiro positivo.

import unittest

def test_soma_1():
    assert soma_digitos(4) == 4
    print('OK - soma certo 01')

def test_soma_2():
    assert soma_digitos(12) == 3
    print('OK - soma certo 02')

def test_soma_3():
    assert soma_digitos(0) == 0
    print('OK - soma certo 03')


def soma_digitos(numero):
    if numero < 10:
        return numero
    else:
        ultimo_digito = numero % 10
        numero_sem_ultimo_digito = numero // 10
        return ultimo_digito + soma_digitos(numero_sem_ultimo_digito)

numero = int(input('Escreva um numero: '))
resultado = soma_digitos(numero)
print("A soma dos dígitos de", numero, "é", resultado)

if __name__ == '__main__':
    test_soma_1()
    test_soma_2()
    test_soma_3()