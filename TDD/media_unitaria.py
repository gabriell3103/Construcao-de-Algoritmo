# Teste Unitário
# Renomeie o nome do arquivo para main para funcionar


import unittest

def calculo_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    if media >= 6:
        return 'Aprovado'
    elif media >= 3:
        return 'Recuperação'
    else:
        return 'Reprovado'

def test_aprovado():
    assert calculo_media(7, 8, 9) == 'Aprovado'
    print('OK - Aprovado')

def test_recuperaçao():
    assert calculo_media(4, 5, 6) == 'Recuperação'
    print('Ok - Recuperação')

def test_reprovado():
    assert calculo_media(2, 3, 2) == 'Reprovado'
    print('Ok - Reprovado')

if __name__ == '__main__':
    test_aprovado()
    test_recuperaçao()
    test_reprovado()