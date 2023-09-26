# 5. Crie um programa que calcule a média dos elementos de uma matriz.
def media_matriz(matriz: list) -> float:
    quantidade_itens = 0
    soma = 0

    for linha in matriz:
        soma += sum(linha)
        quantidade_itens += len(linha)
    
    media = soma / quantidade_itens
    return media


matriz = [
    [1, 2, 4],
    [2, 5, 6],
    [4, 6, 7]
]

media = media_matriz(matriz)
print(media)