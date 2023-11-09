# 7. Escreva uma função recursiva que converta um número inteiro em binário representado como uma string.

def inteiro_para_binario(numero):
    if numero == 0:
        return "0"
    elif numero == 1:
        return "1"
    else:
        return inteiro_para_binario(numero // 2) + str(numero % 2)


numero = int(input('Qual numero você deseja transformar em binario: '))
binario = inteiro_para_binario(numero)
print(f"A representação binária de {numero} é {binario}")
