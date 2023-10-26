# EXERCÍCIO 7.4
# Escreva uma função que calcule o fatorial de um número. O fatorial pode ser definido como:
#         {    1,     se n é 0
# fat(n) -
#         { n x fat(n-1),  se n é maior que 0

def calcular_fatorial(num: int):
    if num == 0:
        return 1
    if num > 0:
        return num * calcular_fatorial(num - 1)

    return "Fatorial indefinido para números negativos"


n = 5
resultado = calcular_fatorial(n)
print(f'O fatorial de {n} é {resultado}')