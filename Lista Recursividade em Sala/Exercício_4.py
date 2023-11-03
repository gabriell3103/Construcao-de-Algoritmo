# 4. Escreva uma função recursiva que imprima uma contagem regressiva a partir de um número n até 0

import unittest

def contagem_regressiva(n):
   if n < 0:
        return 0
   else:
        print(n)
        contagem_regressiva(n - 1)

n = int(input('Quantos segundos de contagem: '))
contagem_regressiva(n)

