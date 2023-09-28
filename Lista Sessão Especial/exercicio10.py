# 10. Escreva uma função que retorne a matriz resultante da multiplicação de duas matrizes.

def multiplicar_matrizes(matriz1: list, matriz2: list) -> list:
    if len(matriz1[0]) != len(matriz2):
        raise ValueError("O número de colunas da matriz1 deve ser igual ao número de linhas da matriz2")


    num_linhas_matriz1 = len(matriz1)
    num_colunas_matriz2 = len(matriz2[0])
    matriz_resultante = [[0 for _ in range(num_colunas_matriz2)] for _ in range(num_linhas_matriz1)]


    for i in range(num_linhas_matriz1):
        for j in range(num_colunas_matriz2):
            for k in range(len(matriz2)):
                matriz_resultante[i][j] += matriz1[i][k] * matriz2[k][j]

    return matriz_resultante


matriz1 = [[1, 2], [3, 4]]
matriz2 = [[5, 6], [7, 8]]
resultado = multiplicar_matrizes(matriz1, matriz2)
print(resultado)
