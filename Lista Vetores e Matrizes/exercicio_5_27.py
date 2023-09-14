# EXERCÍCIO 5.27
# Escreva um programa que crie uma matriz bidimensional usando 2 comandos for encaixados, isto é, não use nem multiplicação nem lista por compreensão para criar sua matriz.

linhas = 3
colunas = 3

matriz = []

for i in range(linhas):
    linha = []

    for j in range(colunas):
        linha.append(0)

    matriz.append(linha)

for linha in matriz:
    print(linha)