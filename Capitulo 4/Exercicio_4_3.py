#Escreva um programa em Python que leia um número e imprima a si mesmo, o seu quadrado e o seu cubo.
def quadrado_cubo(numero):
    
    quadrado_do_numero = numero**2
    cubo_do_numero = numero**3

    print(f"O numero é {numero}, o quadrado dele é {quadrado_do_numero} e o cubo dele é {cubo_do_numero}")

valor = int(input('Digite um número: '))
quadrado_cubo(valor)