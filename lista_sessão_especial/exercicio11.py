# 11. Implemente uma função que calcule o produto vetorial entre dois vetores tridimensionais.

def produto_vetorial(a: int, b: int) -> list:
    if len(a) != 3 or len(b) != 3:
        raise ValueError("Os vetores devem ser tridimensionais (ter tamanho 3)")

    resultado = [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0]
    ]

    return resultado


vetor1 = [1, 2, 3]
vetor2 = [4, 5, 6]
resultado = produto_vetorial(vetor1, vetor2)
print(resultado)
