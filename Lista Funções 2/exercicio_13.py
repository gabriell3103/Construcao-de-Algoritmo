def quadrado(base: int, altura: int):
    for i in range(1,altura + 1):
        print('* ' * base)

base = int(input('Escreva o tamanho da base: '))
altura = int(input('Escreva o tamanho da altura: '))
quadrado(base, altura)