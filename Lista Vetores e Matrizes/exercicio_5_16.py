# EXERCÍCIO 5.16
# Considere a lista
# planetas = [‘Mercúrio’, ‘Vênus’, ‘Terra’, ‘Marte’, ‘Saturno’, ‘Júpiter’, ‘Urano’, ‘Netuno’].
# Execute as seguintes operações usando apenas fatiamento. Cada item usa a lista resultante do item anterior.
# 1.Insira a lista [‘Fobos’,’Deimos’] na posição 4 da lista.
# 2.Insira [‘Sol’] na posição zero.
# 3.Qual seria o fatiamento para imprimir [‘Urano’, ‘Júpiter’, ‘Saturno’, ‘Deimos’, ‘Fobos’, ‘Marte’, ‘Terra’, ‘Vênus’], nessa ordem?

planetas = ['Mercúrio', 'Vênus', 'Terra', 'Marte', 'Saturno', 'Júpiter', 'Urano', 'Netuno']

planetas[4:4] = ['Fobos', 'Deimos']

planetas[:0] = ['Sol']

lista_nova = planetas[6:8] + planetas[5:6] + planetas[4:5] + planetas[3:4] + planetas[7:8] + planetas[2:3] + planetas[1:2] + planetas[0:1]

print(lista_nova)
