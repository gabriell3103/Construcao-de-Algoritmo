# Modifique o programa anterior para que o mesmo capture também a exceção ValueError da entrada de dados pelo usuário.

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