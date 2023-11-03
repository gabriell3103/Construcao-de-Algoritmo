# EXERCÍCIO 7.3
# Escreva uma função recursiva que diga se uma frase é um palíndromo. Não esqueça de ignorar ou apagar os espaços antes de comparar as letras.
# Ex: “A mala nada na lama”, “a base do teto desaba”.

import unittest

def test_palindromo1():
    assert palindromo_frase('olha que bacana') == False
    print('OK - 1')

def test_palindromo2():
    assert palindromo_frase('A mala nada na lama') == True
    print('OK - 2')

def test_palindromo3():
    assert palindromo_frase('') == True
    print('OK - 3')

def palindromo_frase(frase: str):
    frase = frase.replace(" ", "").lower()
    if len(frase) <= 1:
        return True
    elif frase[0] == frase[-1]:
        return palindromo_frase(frase[1:-1])
    else:
        return False


teste1 = "A mala nada na lama"
teste2 = "a base do teto desaba"

print(palindromo_frase(teste1))
print(palindromo_frase(teste2))

if __name__ == '__main__':
    test_palindromo1()
    test_palindromo2()
    test_palindromo3()