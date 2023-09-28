# 9. Crie um programa que calcule o determinante de uma matriz 3x3.

def determinante(matriz: list) -> int:
    dp = 1
    ds = 1
    for i, l in enumerate(matriz):
        for j, v in enumerate(matriz[i]):
            if i == j:
                dp *= matriz[i][j]
            else:
                ds *= matriz[j][i]
    return dp - ds

matriz = [
    [1, 2],
    [3, 4],
]

determinantee = determinante(matriz)
print(determinantee)