# Escreva um programa que imprima uma tabela das raízes quadradas dos números entre 1 e 100, com incrementos de 10.

def raiz_10_em_10():    
    for i in range(1, 101, 10):
        print(f'A raiz de {i} é {i**0.5:.2f}')

raiz_10_em_10()