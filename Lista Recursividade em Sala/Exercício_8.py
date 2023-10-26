# 8. Escreva uma função recursiva que realize uma divisão inteira de dois números inteiros, sem usar o operador de divisão. A função deve retornar o quociente da divisão.

def divisao_inteira(dividendo, divisor):
    if dividendo < divisor:
        return 0
    else:
        return 1 + divisao_inteira(dividendo - divisor, divisor)


dividendo = 15
divisor = 3
quociente = divisao_inteira(dividendo, divisor)
print(f"A divisão de {dividendo} por {divisor} é igual a {quociente}")
