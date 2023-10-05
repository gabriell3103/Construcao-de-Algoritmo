# EXERCÍCIO 6.13
# Escreva um programa que salve uma tabela com a conversão de temperaturas Celsius para Fahrenheit de 0 a 300.

def celsius_para_fahrenheit(celsius: float):
    return (celsius * 9/5) + 32

def conversão_arquivo(arquivo: str) -> None:
    arquivo = open(arquivo, 'w')
    arquivo.write("De célsius para Fahrenheit\n")
    
    for celsius in range(0, 301, 10):
      fahrenheit = celsius_para_fahrenheit(celsius)
      arquivo.write(f'Em célsius = {celsius} | Em Fahrenheit = {fahrenheit}\n')

teste = 'conversão.txt'
conversão_arquivo(teste)