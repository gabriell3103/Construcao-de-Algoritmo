def contar_ocorrencias(lista: list, elemento):
    contador = 0
    for i in lista:
        if i == elemento:
            contador += 1
    return contador

lista = [1, 1, 1, 4, 5]
elemento = 1

quantidade = contar_ocorrencias(lista, elemento)
print(f'A quantidade de {elemento} que aparecem nessa lista é {quantidade}')