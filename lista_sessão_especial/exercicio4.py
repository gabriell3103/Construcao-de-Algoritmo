# 4. Crie uma função que verifique se uma matriz é simétrica.
def e_simetrica(matriz: list) -> bool:
    tam_matriz = len(matriz)
    for i in range(tam_matriz):
        for j in range(tam_matriz):
            if i != j and matriz[i][j] != matriz[j][i]:
                return False
    
    return True

matriz = [
    [1,2,4],
    [2,5,6],
    [4,6,7]
]

print(e_simetrica(matriz))