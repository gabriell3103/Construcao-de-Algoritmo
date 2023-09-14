# EXERCÍCIO 5.28
# Escreva um programa que crie uma matriz tridimensional usando o mecanismo de lista por compreensão.

di_x = 3
di_y = 3
di_z = 3

matriz_3d = [[[0 for _ in range(di_z)] for _ in range(di_y)] for _ in range(di_x)]

for x in range(di_x):
    for y in range(di_y):
        for z in range(di_z):
            print(f"matriz_3d[{x}][{y}][{z}] = {matriz_3d[x][y][z]}")