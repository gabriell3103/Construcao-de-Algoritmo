# 15. Crie um programa que implemente o método de Jacobi para encontrar os autovalores de uma matriz simétrica.

import math

def matriz_transposta(matriz: list) -> list:
    n = len(matriz)
    transposta = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            transposta[i][j] = matriz[j][i]
    return transposta

def matriz_jacobi(A, tolerancia=1e-6, max_iteracoes=1000):
    n = len(A)
    V = [[0] * n for _ in range(n)]
    for i in range(n):
        V[i][i] = 1.0

    iteracao = 0

    while True:
        p, q = 0, 1
        max_valor = abs(A[p][q])
        for i in range(n):
            for j in range(i + 1, n):
                if abs(A[i][j]) > max_valor:
                    max_valor = abs(A[i][j])
                    p, q = i, j

        if max_valor < tolerancia or iteracao >= max_iteracoes:
            autovalores = [A[i][i] for i in range(n)]
            return sorted(autovalores)

        if A[p][p] == A[q][q]:
            theta = math.pi / 4.0
        else:
            theta = 0.5 * math.atan(2 * A[p][q] / (A[p][p] - A[q][q]))


        c = math.cos(theta)
        s = math.sin(theta)
        R = [[0] * n for _ in range(n)]
        for i in range(n):
            R[i][i] = 1.0
        R[p][p] = c
        R[q][q] = c
        R[p][q] = -s
        R[q][p] = s

        RT = matriz_transposta(R)

        A = [[0] * n for _ in range(n)]
        V = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    A[i][j] += R[i][k] * A_original[k][j]
                V[i][j] = V[i][j] + R[i][p] * V_original[p][j] + R[i][q] * V_original[q][j]

        iteracao += 1


A_original = [
    [4, 3],
    [3, 5]
]

V_original = [
    [1, 0],
    [0, 1]
]

autovalores = matriz_jacobi(A_original)
print("Autovalores:", autovalores)
