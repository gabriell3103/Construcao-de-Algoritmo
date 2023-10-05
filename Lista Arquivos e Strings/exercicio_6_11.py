# EXERCÍCIO 6.11
# Escreva um programa que converta todas as letras de um arquivo em minúsculas e escreva o resultado na tela.

def converter_maiusculas(arquivo: str):
    arquivo = open(arquivo, 'r')

    for linha in arquivo:
        linha_minuscula = linha.lower()
        print(linha_minuscula)

    arquivo.close()


teste = 'teste.txt'
converter_maiusculas(teste)