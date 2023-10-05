# EXERCÍCIO 6.10
# Escreva um programa que converta todas as letras de um arquivo em maiúsculas e escreva o resultado na tela.

def converter_maiusculas(arquivo: str):
    arquivo = open(arquivo, 'r')

    for linha in arquivo:
        linha_maiuscula = linha.upper()
        print(linha_maiuscula)

    arquivo.close()


teste = 'teste.txt'
converter_maiusculas(teste)