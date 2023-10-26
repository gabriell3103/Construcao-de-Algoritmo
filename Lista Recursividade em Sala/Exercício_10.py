# 10.Escreva uma função recursiva que determine se um número inteiro n é primo. Um número primo é aquele que é divisível apenas por 1 e por ele mesmo.

def is_primo(n, divisor=2):
    if n <= 1:
        return False
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    return is_primo(n, divisor + 1)

numero = 17
if is_primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")
