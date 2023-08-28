def calculo_media(n1, n2, n3):
    soma = n1 + n2 + n3
    media = soma/3
    return print(f'A sua média é: {media:.2f}')

nota1 = float(input('Digite sua primeira nota? '))
nota2 = float(input('Digite sua segunda nota? '))
nota3 = float(input('Digite sua terceira nota? '))
calculo_media(nota1, nota2, nota3)
