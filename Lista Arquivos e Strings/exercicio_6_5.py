# EXERCÍCIO 6.5
# Tente outras formas de testar se uma palavra é um palíndromo. Tente outro fatiamento.

def teste_palindromo(palavra: str):
    palavra = palavra.upper()

    palavra_invertida = palavra[::-1]

    if palavra == palavra_invertida:
        return print('Essa palavra é palíndroma')
    else:
        return print('Essa palavra não é palíndroma')


teste = teste_palindromo('ovo')
