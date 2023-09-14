# EXERCÍCIO 5.22
# Use os comandos desta seção para apagar os elementos da primeira metade de uma lista.
# Por exemplo, se temos lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], use os comandos para obter lista = [5, 6, 7, 8, 9].

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

final = lista[len(lista)//2:]

print(final)