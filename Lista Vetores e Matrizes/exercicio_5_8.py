# EXERCÍCIO 5_8
# Escreva um programa para gerar uma lista com o quadrado dos números ímpares de 0 a 9, como no Programa 5.16,
# porém não use filtros. Use apenas o comando range() para controlar a geração da sequência de números ímpares.

imapres_ao_quadrado = []

for numero in range(10):
    if numero % 2 == 1:
        quadrado = numero ** 2
        imapres_ao_quadrado.append(quadrado)

print(imapres_ao_quadrado)
