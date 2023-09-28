# 13. Implemente um programa que resolva um sistema de equações lineares usando a matriz aumentada e o método de eliminação de Gauss.

def print_matrix(matriz: list):
    for linha in matriz:
        print(linha)

def eliminacao_de_gauss(matriz_aumentada: list):
    num_linhas = len(matriz_aumentada)
    num_colunas = len(matriz_aumentada[0]) - 1

    for i in range(num_linhas):
        max_pivo = abs(matriz_aumentada[i][i])
        max_linha = i
        for k in range(i + 1, num_linhas):
            if abs(matriz_aumentada[k][i]) > max_pivo:
                max_pivo = abs(matriz_aumentada[k][i])
                max_linha = k

        matriz_aumentada[i], matriz_aumentada[max_linha] = matriz_aumentada[max_linha], matriz_aumentada[i]

        for k in range(i + 1, num_linhas):
            fator = matriz_aumentada[k][i] / matriz_aumentada[i][i]
            for j in range(i, num_colunas + 1):
                matriz_aumentada[k][j] -= fator * matriz_aumentada[i][j]

    solucao = [0] * num_linhas
    for i in range(num_linhas - 1, -1, -1):
        solucao[i] = matriz_aumentada[i][num_colunas] / matriz_aumentada[i][i]
        for k in range(i - 1, -1, -1):
            matriz_aumentada[k][num_colunas] -= matriz_aumentada[k][i] * solucao[i]

    return solucao


matriz_aumentada = [
    [2, 1, -1, 8],
    [-3, -1, 2, -11],
    [-2, 1, 2, -3]
]

solucao = eliminacao_de_gauss(matriz_aumentada)

print("Solução:")
for i, valor in enumerate(solucao):
    print(f'x{i+1} = {valor}')
