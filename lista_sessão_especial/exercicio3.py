# 3. Crie uma função que receba uma matriz e retorne a transposta dela.

def matriz_transposta(matriz: list) -> list:
    tam_coluna = len(matriz[0])
    tam_linha = len(matriz)
    transposta = []
    
    for _ in range(tam_coluna):
        transposta.append([0 for _ in range(tam_linha)])
    
    for i, l in enumerate(matriz):
        for j, v in enumerate(l):
            transposta[j][i] = v
    
    return transposta


matriz = [
    [1, 7],
    [8, 2],
    [4, 9]
]

t = matriz_transposta(matriz)
print(t)