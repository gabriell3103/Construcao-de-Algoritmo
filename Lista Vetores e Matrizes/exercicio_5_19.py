# EXERCÍCIO 5.19
# O que acontece se o terceiro parâmetro de uma operação de fatiamento for -1? Teste em uma lista qualquer o comando lista[::-1]. Qual a diferença para reverse()?

lista = [1, 2, 4, 8, 16]
invertida = lista[::-1]
print(invertida)

lista.reverse()
print(invertida)

# A diferença entre elas é que o reverse() apenas da a mesma lista invertida enquanto o fatiamento gera uma nova lista invertida.