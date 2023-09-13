# EXERCÍCIO 5.2
# Reescreva o programa 5.13 de modo a imprimir o resultado a partir do último elemento (de 300 para 0).

print('Tabela de conversão de Fahrenheit para Celsius')

for fahr in range(300, -1, -20):

    celsius = (5/9)*(fahr - 32)

    print('{:>5d} -> {:>5.1f}'.format(fahr, celsius))