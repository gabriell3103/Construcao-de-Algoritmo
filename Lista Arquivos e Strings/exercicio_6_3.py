# EXERCÍCIO 6.3
# Escreva um programa em Python que conte a quantidade de espaços em branco de uma string.

frase = input('Escreva uma frase: ')
contador = 0
for i in frase:
    if i == ' ':
        contador += 1

print(f'A quantidade de espaços em branco que essa frase possui é: {contador}')