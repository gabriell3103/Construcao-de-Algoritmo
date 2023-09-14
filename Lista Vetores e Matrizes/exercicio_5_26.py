# EXERCÍCIO 5.26
# Escreva um programa que crie uma lista com números digitados pelo usuário e forneça como saída a média desses números.

numeros = []

while True:
    nota = input("Digite um número ou 'fim' para finalizar: ")

    if nota.lower() == 'fim':
        break
    try:
        numero = float(nota)
        numeros.append(numero)
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")
if numeros:
    media = sum(numeros) / len(numeros)
    print(f"A média dos números digitados é: {media:.2f}")
else:
    print("Nenhum número foi digitado.")