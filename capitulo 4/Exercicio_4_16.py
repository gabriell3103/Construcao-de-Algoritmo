# Escreva um programa que crie uma lista com 3 elementos e peça ao usuário um índice de um elemento a ser impresso.
# Se o usuário pedir um índice fora da faixa de valores permitidos (abaixo de zero ou acima de 2).
# O programa deve emitir uma mensagem de erro (Use a exceção IndexError).

import random

lista = []
aleatorio1 = random.randint(1,10)
aleatorio2 = random.randint(1,10)
aleatorio3 = random.randint(1,10)

lista.append(aleatorio1)
lista.append(aleatorio2)
lista.append(aleatorio3)

escolha = int(input('Digite um indice de 0 a 2 para a lista: '))

if escolha > -1 and escolha < 3:
    print(lista[escolha])
else:
    print('Esse indice não existe dentro da lista!')