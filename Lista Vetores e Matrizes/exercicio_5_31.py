# EXERCÍCIO 5.31
# Escreva um programa que crie uma tupla com todos os números entre 100 e 1000 que são divisíveis por 7 mas não são múltiplos de 3.


lista = []


for numero in range(100, 1001):
    if numero % 7 == 0 and numero % 3 != 0:
        lista.append(numero)

tupla = tuple(lista)
print(tupla)
