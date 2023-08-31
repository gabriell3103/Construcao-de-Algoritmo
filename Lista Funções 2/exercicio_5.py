def calcular_potencia(base, expoente):
    potencia = base ** expoente
    return potencia

base = int(input('Digite a base: '))
expoente = int(input('Digite o expoente: '))
potencia = calcular_potencia(base, expoente)
print(f'A potencia é: {potencia}')