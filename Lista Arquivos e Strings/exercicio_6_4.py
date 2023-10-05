# EXERCÍCIO 6.4
# Escreva uma função que receba uma string como parâmetro e escreva-a invertida, usando apenas o fatiamento.
# Ex.: ‘celacanto provoca maremoto’ imprime ‘otomeram acovorp otnacalec’. Dica: o passo pode ser negativo.

def função_invertida(string: str) -> str:
    frase_invertida = string[::-1]
    return frase_invertida


string = 'celacanto provoca maremoto'
teste = função_invertida(string)
print(teste)