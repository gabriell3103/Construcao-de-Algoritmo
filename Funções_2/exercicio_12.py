def calcular_raiz_quadrada(num):
    raiz_quadrada = num ** 0.5
    return raiz_quadrada

num = float(input('Digite um número: '))
print(f'A raiz quadrada de {num} é {calcular_raiz_quadrada(num): .2f}')