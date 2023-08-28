# Escreva uma função que dada uma nota entre 0.0 e 10.0 imprima na tela um conceito entre ‘A’ e ‘E’, segundo a tabela:
# A ≥ 9.0     9.0 > B ≥ 8.0 8.0 > C ≥ 7.0     7.0 > D ≥ 5.0     E < 5.0
# O que acontece com o seu programa se for digitada nota menor que zero ou maior que dez?

def conceito_notas():
    nota = float(input("Escreva sua nota: "))

    if nota < 10.1 and nota > 8.9:
        print("A")
    elif nota < 9 and nota > 7.9:
        print("B")
    elif nota < 8 and nota > 6.9:
        print("C")
    elif nota < 7 and nota > 4.9:
        print("D")
    elif nota > 0 and nota < 5:
        print("E")
    else:
        print("As notas vão de 0 a 10!")


conceito_notas()
