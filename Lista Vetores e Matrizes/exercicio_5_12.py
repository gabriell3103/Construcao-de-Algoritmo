# EXERCÍCIO 5.12
# Escreva um programa que dada a lista [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] gere a lista [1, 3, 5, 7, 9, 0, 2, 4, 6, 8].

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

nova_lista = []

for elemento in lista:
    if elemento % 2 == 1:
        nova_lista.append(elemento)

for elemento in lista:
    if elemento % 2 == 0:
        nova_lista.append(elemento)

print(nova_lista)