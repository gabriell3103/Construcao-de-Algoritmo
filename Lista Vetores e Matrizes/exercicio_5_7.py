# EXERCÍCIO 5.7
# Escreva um programa para gerar uma lista com o quadrado dos números pares entre 10 e 20 (inclusive).


pares_ao_quadrados = []
for numero in range(10, 21):
    if numero % 2 == 0:
        quadrado = numero ** 2
        pares_ao_quadrados.append(quadrado)

print(pares_ao_quadrados)