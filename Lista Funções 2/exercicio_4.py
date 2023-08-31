def calculo_media(lista: list):
    soma = 0
    for i in lista:
        soma += i
        media = soma / len(lista)
    return media

notas = [10,5,8]
media = calculo_media(notas)
print(f'A média é: {media}')
