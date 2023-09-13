# EXERCÍCIO 5.4
# Reescreva o Programa 5.13 usando o comando while.

print('Tabela de conversão de Fahrenheit para Celsius')

fah = 0

while fah <= 300:
    celsius = (5/9)*(fah - 32)
    print('{:>5d} -> {:>5.1f}'.format(fah, celsius))
    fah += 20