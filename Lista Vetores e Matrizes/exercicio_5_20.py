# EXERCÍCIO 5.20
# Escreva um programa que inverta uma lista usando o método de lista por compreensão.

lista = [1, 2, 4, 8, 16]
invertida = [lista[i] for i in range(len(lista) - 1, -1, -1)]
print(invertida)