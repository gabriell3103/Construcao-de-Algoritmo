# EXERCÍCIO 5.11
# Escreva um programa que dada a lista [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] gere a lista [5, 6, 7, 8, 9, 0, 1, 2, 3, 4].

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numeros = 5

nova_lista = lista[numeros:] + lista[:numeros]

print(nova_lista)