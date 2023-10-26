def percorrer_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f'[{i}, {j}]')

a = [50, 10, 20]
b = [75, 82, 91]
c = [25, 11, 53]
d = [a, b, c]
# print(d[1][2]) = 91
percorrer_matriz(d)