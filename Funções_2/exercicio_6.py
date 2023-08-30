def Encontrar_primos(num: int):
    primos = []
    for i in range(2, num + 1):
        if Verifica_primo(i):
            primos.append(i)
    return primos


def Verifica_primo(num: int):
    for i in range(2, num):
        divide = num % i == 0
        if divide:
            return False
        return True

lista_primos = Encontrar_primos(5)
print(lista_primos)