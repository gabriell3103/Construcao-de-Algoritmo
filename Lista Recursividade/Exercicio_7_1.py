# EXERCÍCIO 7.1
# Escreva uma função recursiva que imprima uma string na ordem inversa. Ex.: “celacanto provoca maremoto” será impressa como “otomeram acovorp otnacalec”.

import unittest

def test_inversa1():
    assert string_inversa('alo') == 'ola'
    print('OK - 1')
def test_inversa2():
    assert string_inversa('') == ''
    print('OK - 2')

def string_inversa(string: str):
    if len(string) == 0:
        return ""

    return string[-1] + string_inversa(string[:-1])


string = "celacanto provoca maremoto"
resultado = string_inversa(string)
print(resultado)

if __name__ == '__main__':
    test_inversa1()
    test_inversa2()