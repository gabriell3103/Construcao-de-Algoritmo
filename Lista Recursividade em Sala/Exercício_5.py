# 5. Escreva uma função recursiva que calcule a potência de um número base elevado a um expoente.

def potencia(base, expoente):
    if expoente == 0:
        return 1
    else:
        return base * potencia(base, expoente - 1)

base = 2
expoente = 3
resultado = potencia(base, expoente)
print(base, "elevado a", expoente, "é igual a", resultado)
