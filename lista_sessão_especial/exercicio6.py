# 6. Implemente uma função que calcule o produto escalar entre dois vetores.

def produto_escalar(vetor1: list, vetor2: list):
    vetor3 = []
    for i in range(len(vetor1)):
        vetor3.append(vetor1[i] * vetor2[i])

    return vetor3
        

vetor1 = [1, 3, 5]
vetor2 = [0, 2, 4]
produto = produto_escalar(vetor1, vetor2)

print(f'O produto escalar {produto}')