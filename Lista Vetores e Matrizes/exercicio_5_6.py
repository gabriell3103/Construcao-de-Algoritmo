#EXERCÍCIO 5.6
# Modifique o Programa 4.23 que calcula pi para que este não mais solicite o número de pontos a serem gerados,
# mas gere uma tabela com ao menos 10 valores de pi calculados com números diferentes de pontos.
# Sua tabela deve possuir ao menos 10 valores diferentes. Use range() para gerar os diversos valores de entrada da função.

import random
import math

def gerar_coords_aleatorias():
    '''Gera par de coordenadas aleatórias.'''

    x = random.random()

    y = random.random()

    return x, y

def coords_circulo(x, y):
    '''Testa se coordenadas estão dentro do círculo de raio 1.'''

    return math.hypot(x, y) < 1

def calcula_pi(n):
    '''Calcula pi e o erro associado a partir de n pontos.'''
    conta_circulo = 0

    for _ in range(n):
        x, y = gerar_coords_aleatorias()

        if coords_circulo(x, y):
            conta_circulo += 1

    pi = 4 * conta_circulo / n
    erro = math.fabs(pi - math.pi)

    return pi, erro

def main():
    num_valores_pi = 10
    tabela_pi = []
    
    for num_pontos in range(1, num_valores_pi + 1):
        pi, erro = calcula_pi(num_pontos)
        tabela_pi.append((num_pontos, pi, erro))

    print("Pontos | Pi | Erro")
    for linha in tabela_pi:
        print(f"{linha[0]:.2f} | {linha[1]:.2f} | {linha[2]:.4f}")

main()