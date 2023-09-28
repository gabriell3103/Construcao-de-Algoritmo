# 12. Crie uma função que encontre os autovalores e autovetores de uma matriz.

import random

def produto_matriz_vetor(matriz: list, vetor:list) -> list:
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])
    
    resultado = [0] * num_linhas

    for i in range(num_linhas):
        for j in range(num_colunas):
            resultado[i] += matriz[i][j] * vetor[j]

    return resultado

def normalizar_vetor(vetor: list):
    norma = sum(x ** 2 for x in vetor) ** 0.5
    return [x / norma for x in vetor]

def encontrar_autovalor_e_autovetor(matriz: list, num_iteracoes=1000, tolerancia=1e-6):
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])
    
    vetor = [random.random() for _ in range(num_colunas)]
    
    for _ in range(num_iteracoes):
        resultado_produto = produto_matriz_vetor(matriz, vetor)
        autovalor = max(resultado_produto, key=abs)
        vetor_normalizado = normalizar_vetor(resultado_produto)
        erro = sum((x - y) ** 2 for x, y in zip(vetor, vetor_normalizado)) ** 0.5
        
        if erro < tolerancia:
            break
        
        vetor = vetor_normalizado

    return autovalor, vetor

matriz = [[2, -1], [1, 3]]
autovalor, autovetor = encontrar_autovalor_e_autovetor(matriz)
print("Autovalor:", autovalor)
print("Autovetor:", autovetor)

