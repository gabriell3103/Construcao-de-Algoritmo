# EXERCÍCIO 5_9
# Escreva um programa que crie uma lista com o cubo dos números entre 1 e 10, ambos inclusive.



lista_de_cubos = []

for numero in range(1, 11):
    cubo = numero ** 3
    lista_de_cubos.append(cubo)

print(lista_de_cubos)

