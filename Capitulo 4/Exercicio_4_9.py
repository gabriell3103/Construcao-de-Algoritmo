# Escreva uma função fahrenheit(celsius) que receba um valor de uma temperatura Celsius e devolva seu equivalente em Fahrenheit.
# Usando esta função, imprima os valores equivalentes das temperaturas Celsius em Fahrenheit entre 0 e 100, com incrementos de 10.

def fahrenheit():
    for i in range(0,101):
        print(f' F{i} --> {i * (9/5) + 32 + 10}C')

fahrenheit()
    
