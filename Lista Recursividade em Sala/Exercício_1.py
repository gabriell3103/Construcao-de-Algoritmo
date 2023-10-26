# 1. Escreva uma função recursiva para calcular o fatorial de um número n.

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
    
num = int(input('Escreva um número: '))
fat = fatorial(num)
print(fat)