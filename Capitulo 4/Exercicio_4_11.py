# Escreva uma função distancia(x1, y1, x2, y2) que devolva a distância entre dois pontos cujas coordenadas cartesianas são (x1, y1) e (x2, y2).

import math


def distancia(x1, y1, x2, y2):

    diferença_x = x2 - x1
    diferença_y = y2 - y1

    distancia = math.sqrt(diferença_x ** 2 + diferença_y ** 2)
    return distancia


x1 = int(input('Escreva um núumero: '))
x2 = int(input('Escreva um núumero: '))
y1 = int(input('Escreva um núumero: '))
y2 = int(input('Escreva um núumero: '))

distancia = distancia(x1, y1, x2, y2)
print(distancia)
