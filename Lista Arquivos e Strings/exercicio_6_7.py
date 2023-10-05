# EXERCÍCIO 6.7
# Escreva uma função que receba uma string como parâmetro e diga se se trata de um palíndromo ou não.
# Na string devem ser ignorados os espaços em branco e as letras maiúsculas e minúsculas não são diferenciadas.
# Por exemplo, a frase ‘Seco de raiva coloco no colo caviar e doces’ deve ser considerada um palíndromo.

def teste_palindromo(frase: str):
    frase = frase.lower()
    frase = frase.replace(' ', '')

    frase_invertida = frase[::-1]

    if frase == frase_invertida:
        return print('Essa palavra é palíndroma')
    else:
        return print('Essa palavra não é palíndroma')


teste = teste_palindromo('Seco de raiva coloco no colo caviar e doces')
