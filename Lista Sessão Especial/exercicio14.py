# 14. Desenvolva uma função que calcule a matriz inversa de uma matriz quadrada.

def matriz_transposta(matriz: list) -> list:
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])
    transposta = [[0] * num_linhas for _ in range(num_colunas)]
    for i in range(num_linhas):
        for j in range(num_colunas):
            transposta[j][i] = matriz[i][j]
    return transposta

def matriz_adjunta(matriz: list) -> list:
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])
    adjunta = [[0] * num_colunas for _ in range(num_linhas)]
    for i in range(num_linhas):
        for j in range(num_colunas):
            cofator = [[matriz[m][n] for n in range(num_colunas) if n != j] for m in range(num_linhas) if m != i]
            determinante_cofator = determinante(cofator)
            adjunta[i][j] = ((-1) ** (i + j)) * determinante_cofator
    return adjunta

def determinante(matriz: list):
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])

    if num_linhas != num_colunas:
        raise ValueError("A matriz não é quadrada, portanto, não possui determinante.")

    if num_linhas == 1:
        return matriz[0][0]
    elif num_linhas == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    else:
        det = 0
        for j in range(num_colunas):
            cofator = [[matriz[i][j] for i in range(num_linhas) if i != 0] for j in range(num_colunas) if j != j]
            det += matriz[0][j] * ((-1) ** j) * determinante(cofator)
        return det

def matriz_inversa(matriz: list) -> list:
    det = determinante(matriz)
    
    if det == 0:
        raise ValueError("A matriz não possui inversa, pois o determinante é zero.")

    adjunta = matriz_adjunta(matriz)
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])

    inversa = [[0] * num_colunas for _ in range(num_linhas)]

    for i in range(num_linhas):
        for j in range(num_colunas):
            inversa[i][j] = adjunta[i][j] / det

    return inversa

matriz = [
    [2, 1],
    [1, 3]
]

inversa = matriz_inversa(matriz)

print("Matriz Inversa:")
for linha in inversa:
    print(linha)
