# 2. Escreva uma função recursiva que calcule a soma dos dígitos de um número inteiro positivo.

def soma_digitos(numero):
    if numero < 10:
        return numero
    else:
        ultimo_digito = numero % 10
        numero_sem_ultimo_digito = numero // 10
        return ultimo_digito + soma_digitos(numero_sem_ultimo_digito)

numero = 123
resultado = soma_digitos(numero)
print("A soma dos dígitos de", numero, "é", resultado)