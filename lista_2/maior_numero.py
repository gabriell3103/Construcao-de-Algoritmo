import math


def maior_numero(lista_numeros):
    lista_organizada = sorted(lista_numeros)
    lista_tamanho = (len(lista_organizada) - 1)
    return print(lista_organizada[lista_tamanho])


def maior_2(lista):
    maior = max(lista)

    return print(maior)


def maior_3(lista):
    maior = -math.inf
    for i in lista:
        if maior < i:
            maior = i
        return maior


lista = [1, 4, 2, 6, 5]
maior_2(lista)
