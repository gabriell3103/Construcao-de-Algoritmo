# EXERCÍCIO 5.32
# Modifique o Programa 4.16 de modo que a função que gera coordenadas aleatórias receba como parâmetro o número de coordenadas que precisam ser geradas
# Devolva uma lista de tuplas com essas coordenadas. Deste modo,
# A função que calcula o valor de pi também precisa ser modificada para tratar essas coordenadas em forma de lista de tuplas.

import random
import math


def gerar_coords_aleatorias(n):
    '''Gera uma lista de n pares de coordenadas aleatórias.'''

    coordenadas = [(random.random(), random.random()) for _ in range(n)]

    return tuple(coordenadas)


def coords_dentro_circulo(x, y):
    '''Testa se coordenadas estão dentro do círculo de raio 1.'''

    return math.hypot(x, y) < 1


def calcula_pi(coordenadas):
    '''Calcula pi e o erro associado a partir de uma lista de coordenadas.'''

    conta_circulo = 0

    for x, y in coordenadas:
        if coords_dentro_circulo(x, y):
            conta_circulo += 1

    pi = 4 * conta_circulo / len(coordenadas)
    erro = math.fabs(pi - math.pi)

    return pi, erro


num = int(input('Quantos pontos devem ser sorteados? '))

coordenadas = gerar_coords_aleatorias(num)
pi, erro = calcula_pi(coordenadas)

print('Com', num, 'pontos, o valor de pi é', pi, 'com erro', erro)