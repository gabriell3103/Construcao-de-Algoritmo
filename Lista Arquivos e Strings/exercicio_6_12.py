# EXERCÍCIO 6.12
# Escreva um programa que converta a primeira letra de cada palavra de um arquivo em maiúscula e escreva o resultado na tela.

def primeira_letra_maiuscula(arquivo: str) -> None:
    arquivo = open(arquivo, 'r')

    for linhas in arquivo:
        dividir_palavras = linhas.split()
        for palavras in dividir_palavras:
            primeira_maiuscula = palavras.capitalize()
            print(primeira_maiuscula)

    arquivo.close()

teste = 'teste.txt'
primeira_letra_maiuscula(teste)