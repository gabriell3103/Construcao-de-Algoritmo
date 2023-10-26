# 9. Escreva uma função recursiva que conte o número de palavras em uma string. Considere que as palavras são separadas por espaços em branco.

def contar_palavras(frase):
    frase = frase.strip()
    
    if not frase:
        return 0
    else:
        posicao_espaco = frase.find(' ')
        if posicao_espaco == -1:
            return 1
        else:
            return 1 + contar_palavras(frase[posicao_espaco+1:])


frase = "Esta é uma frase de exemplo"
numero_de_palavras = contar_palavras(frase)
print("O número de palavras na frase é:", numero_de_palavras)
