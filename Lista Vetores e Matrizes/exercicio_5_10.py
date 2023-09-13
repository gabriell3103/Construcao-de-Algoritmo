# EXERCÍCIO 5.10
# Escreva um programa que crie uma lista com os 10 primeiros múltiplos de 7.

multiplos_de_sete = []

for i in range(0, 71):
    if i % 7 == 0:
        multiplos_de_sete.append(i)

print(multiplos_de_sete)