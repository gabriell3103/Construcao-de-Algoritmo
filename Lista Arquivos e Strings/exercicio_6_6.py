# EXERCÍCIO 6.6
# O teste de palíndromo desta seção tem um grande problema: ele não diferencia maiúsculas de minúsculas.
# Desse modo, ‘Ovo’ não seria identificado como palíndromo. Como se pode consertar isso? Pesquise a função de Python ‘lower()’ que transforma maiúsculas em minúsculas.

def teste_palindromo(palavra: str):
    palavra = palavra.lower()

    palavra_invertida = palavra[::-1]

    if palavra == palavra_invertida:
        return print('Essa palavra é palíndroma')
    else:
        return print('Essa palavra não é palíndroma')


teste = teste_palindromo('Ovo')
