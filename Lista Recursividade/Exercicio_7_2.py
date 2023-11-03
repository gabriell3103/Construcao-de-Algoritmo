# EXERCÍCIO 7.2
# Escreva uma função recursiva que diga se uma palavra é um palíndromo. Ex: arara, ovo, radar, osso.

import unittest

def test_palindromo1():
    assert palindromo('ovo') == True
    print('OK - 1')
def test_palindromo2():
    assert palindromo('ola') == False
    print('OK - 2')
def test_palindromo3():
    assert palindromo('') == True
    print('OK - 3')

def palindromo(palavra: str):
    palavra = palavra.lower()
    if len(palavra) <= 1:
        return True
    elif palavra[0] == palavra[-1]:
        return palindromo(palavra[1:-1])
    else:
        return False


teste1 = "arara"
teste2 = "ovo"
teste3 = "radar"
teste4 = "osso"

print(palindromo(teste1))
print(palindromo(teste2))
print(palindromo(teste3))
print(palindromo(teste4))

if __name__ == '__main__':
    test_palindromo1()
    test_palindromo2()
    test_palindromo3()