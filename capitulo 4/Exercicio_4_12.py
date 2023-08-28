# Modifique o programa que calcula pi para perguntar diversas vezes pelo número de pontos a serem sorteados.
# Calculando pi para cada pedido. O programa deve terminar quando for digitado ‘0’.

import math
import random


def gera_coordenadas_aleatorias():
    ''' Gera par de coordenadas aleatórias.'''

    x = random.random()

    y = random.random()

    return x, y


def coordenadas_dentro_circulo(x, y):
    ''' Testa  se coordenadas estão dentro do círculo de raio 1.'''

    return math.hypot(x, y) < 1


def calcula_pi(n):
    ''' Calcula pi e o erro associado a partir de n pontos.'''

    conta_circulo = 0

    for i in range(n):

        x, y = gera_coordenadas_aleatorias()

        if coordenadas_dentro_circulo(x, y):

            conta_circulo += 1

    pi = 4 * conta_circulo / n

    erro = math.fabs(pi - math.pi)

    return pi, erro


while True:
    num = int(input('Quantos pontos devem ser sorteados? (Digite 0 para sair): '))

    if num == 0:
        print("Programa encerrado.")
        break

    pi, erro = calcula_pi(num)
    print('Com', num, 'pontos, o valor de pi é', pi, 'com erro', erro)
