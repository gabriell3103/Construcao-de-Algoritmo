# EXERCÍCIO 5.1
# Escreva um programa que receba uma lista de temperaturas em Celsius e escreva na tela o resultado da conversão dessas temperaturas em Fahrenheit.
# (Não se esqueça de usar a fórmula correta!)

def celsius_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def converter(list_temps: list):
    for celsius in list_temps:
        fahrenheit = celsius_fahrenheit(celsius)
        print(f"{celsius}°C = {fahrenheit:.2f}°F")


lista_celcius = [36, 30, 50]
print("Celcius para Fahrenheit:")
converter(lista_celcius)