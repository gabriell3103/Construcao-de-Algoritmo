# Escreva uma função celsius(fahrenheit) que receba um valor de uma temperatura Fahrenheit e devolva seu equivalente em Celsius.
# Usando esta função, imprima os valores equivalentes das temperaturas Fahrenheit em Celsius entre 0 e 300, com incrementos de 10.
# Coloque comandos para que o usuário escolha os valores de início, fim e passo que serão usados como argumentos da função.

def celsius():
    inicio = int(input('Digite o valor inicial: '))
    final = int(input('Digite o valor final: '))

    for i in range(inicio, final + 1):
        print(f'{i}C --> {(32 - i) / (9/5)}F')

celsius()