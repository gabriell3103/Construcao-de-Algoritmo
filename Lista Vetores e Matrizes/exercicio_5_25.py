# EXERCÍCIO 5.25
# Escreva um programa que crie uma lista com todos os números entre 100 e 1000 que são divisíveis por 7 mas não são múltiplos de 3.

lista = []

for i in range(100, 1000):
    if i % 7 == 0 and i % 3 != 0:
        lista.append(i)

print(lista)