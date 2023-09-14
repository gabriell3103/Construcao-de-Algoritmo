# EXERCÍCIO 5.18
# Execute as mesmas operações do exercício 5.17, 
# mas usando o comando extend() no lugar de append() com uma lista. O que acontece? Houve alguma diferença? Tente imprimir o elemento primos[4]. O que é impresso?

lista_primos = [2, 3, 5, 7]
lista_primos.extend([23, 29, 31])

print(lista_primos[4])