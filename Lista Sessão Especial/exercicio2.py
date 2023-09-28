# 2. Crie uma função que receba dois vetores e retorne a soma deles.

def soma_vetores(lista1: list, lista2: list):
    lista3 = []
    for i in range(len(lista1)):
        lista3.append(lista1[i] + lista2[i])

    return lista3

lista1 = [1, 3, 5, 7]
lista2 = [0, 2, 4, 6]

soma = soma_vetores(lista1, lista2)
print(f'A soma entre os vetores é: {soma}')