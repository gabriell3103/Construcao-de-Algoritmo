# 3. Escreva uma função recursiva que calcule a soma dos quadrados dos primeiros n números inteiros.

def soma_quadrados(n):
    if n == 1:
        return 1
    else:
        return n * n + soma_quadrados(n - 1)

n = 5
resultado = soma_quadrados(n)
print("A soma dos quadrados dos primeiros", n, "números inteiros é", resultado)