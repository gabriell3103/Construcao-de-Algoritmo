# Escreva um programa capaz de criar outras formas, usando uma função semelhante à que imprimiu a árvore.

def imprime_linha(n1, carac1, n2, carac2):

    print(carac1 * n1 + carac2 * n2)




def imprime_piramide():
    imprime_linha(5, ' ', 1, '*')
    imprime_linha(4, ' ', 3, '*')
    imprime_linha(3, ' ', 5, '*')
    imprime_linha(2, ' ', 7, '*')
    imprime_linha(1, ' ', 9, '*')
    imprime_linha(0, ' ', 11, '*')


imprime_piramide()
