def quadrado(base: int, altura: int):
    for i in range(altura):
        if i == 0 or i == altura - 1:
            print('* ' * base)
        else:
            print('* ' + '  ' * (base - 2) + '*')


base = int(input('Escreva o tamanho da base: '))
altura = int(input('Escreva o tamanho da altura: '))
quadrado(base, altura)
