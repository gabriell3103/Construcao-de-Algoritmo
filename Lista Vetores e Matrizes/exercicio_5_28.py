# EXERCÍCIO 5.28
# Escreva um programa que crie uma matriz tridimensional usando o mecanismo de lista por compreensão.

tridimensisonal = [[[(j + i + k) * 10 for j in range(3)]for i in range(3)]for k in range(3)]

print(tridimensisonal)