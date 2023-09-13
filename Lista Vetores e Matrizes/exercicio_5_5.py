# EXERCÍCIO 5.5
# Crie uma lista com os números ímpares entre 0 e 100 (use range()) e depois use o comando enumerate().
# para percorrer a lista transformando o valor de cada elemento no valor par subsequente.

impares = []
for i in range(1, 100, 2):
    impares.append(i)
print(impares)
for j,l in enumerate(impares):
    impares [j] = l + 1
print(impares)