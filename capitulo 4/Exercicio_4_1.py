# Expanda a tabela de senos e cossenos para incluir também a tangente, usando a função math.tan().
# Cuidado! Você tem de se preocupar com as tangentes de 90 e 270 graus.
# Por quê? Trate estes casos especiais, evitando incorrer em erro. Use math.inf e -math.inf para indicar valores infinitos, positivos e negativos.


import math

print('{:>9}{:>9}{:>9}{:>9}{:>9}'.format(
    'Graus', 'Radianos', 'Seno', 'Cosseno', 'Tangente'))

for graus in range(0, 361, 30):
    radianos = math.radians(graus)
    seno = math.sin(radianos)
    cosseno = math.cos(radianos)

    if graus == 90:
      tangente = math.inf
        
    elif graus == 270:
      tangente = -math.inf
    else:
      tangente = math.tan(radianos)
        

    print('{:>9.2f}{:>9.2f}{:>9.2f}{:>9.2f}{:>9.2f}'.format(
      graus, radianos, seno, cosseno, tangente))
