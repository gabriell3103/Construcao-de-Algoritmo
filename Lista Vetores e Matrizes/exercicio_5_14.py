# EXERCÍCIO 5.14
# Gere uma lista com 100 números de 0 a 99, com o comando range() e, usando valores negativos no fatiamento, escreva um programa que imprima:
# 1.o último elemento da lista original e depois, decrescendo, os elementos distantes 3 posições a partir do final até o início;
# 2.os elementos entre o índice 87 (inclusive) e o índice 34 (exclusive), em ordem decrescente de índices;
# 3.todos os elementos, exceto os dois últimos.

lista = list(range(100))

print('O último número da lista decrescendo de 3 em 3 do final até o início:')
print(lista[-1])
for i in range(-4, -len(lista) - 1, -3):
    print(lista[i])

print('Numeors entre o índice 87 e o índice 34 em ordem decrescente:')
for i in range(87, 33, -1):
    print(lista[i])

print('Todos os números, menos os últimos 2:')
print(lista[:-2])

