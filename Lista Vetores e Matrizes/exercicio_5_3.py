# EXERCÍCIO 5.3
# Reescreva o programa 5.14 validando a entrada de dados do usuário, usando a estrutura try...except.

def fahr_para_celsius(f):
    '''Converte temperaturas Fahrenheit para Celsius.'''
    return (5 / 9) * (f - 32)

def cria_tabela_celsius(fahr):
    '''Cria tabela Celsius a partir de tab Fahr'''
    celsius = [None] * len(fahr)
    for i, temp in enumerate(fahr):
        celsius[i] = fahr_para_celsius(fahr[i])
    return celsius

def main():
    '''Programa principal.'''
    try:
        start = int(input('Aonde você quer que comece temperaturas Fahrenheit? '))
        stop = int(input('Aonde você quer que termine as temperaturas Fahrenheit? '))
        step = int(input('Qual o intervalo entre as temperaturas Fahrenheit? '))

        fah = list(range(start, stop + 1, step))

        celsius = cria_tabela_celsius(fah)

        print('Tabela de conversão de Fahrenheit para Celsius')

        for i, temp in enumerate(fah):
            print('{:>5d} -> {:>5.1f}'.format(temp, celsius[i]))

    except ValueError:
        print('Certifique-se de inserir valores numéricos válidos.')

main()