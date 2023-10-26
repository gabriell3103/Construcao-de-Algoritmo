# 6. Escreva uma função recursiva que calcule a soma de todos os elementos em uma lista.

def soma_lista(lista):
    if not lista:
        return 0
    else:
        return lista[0] + soma_lista(lista[1:])

minha_lista = [1, 2, 3, 4, 5]
resultado = soma_lista(minha_lista)
print("A soma de todos os elementos da lista é", resultado)
