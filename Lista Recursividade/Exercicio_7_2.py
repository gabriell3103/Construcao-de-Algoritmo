# EXERCÍCIO 7.2
# Escreva uma função recursiva que diga se uma palavra é um palíndromo. Ex: arara, ovo, radar, osso.

def palindromo(palavra: str):
    palavra = palavra.lower()
    if len(palavra) <= 1:
        return True
    elif palavra[0] == palavra[-1]:
        return palindromo(palavra[1:-1])
    else:
        return False


teste1 = "arara"
teste2 = "ovo"
teste3 = "radar"
teste4 = "osso"

print(palindromo(teste1))
print(palindromo(teste2))
print(palindromo(teste3))
print(palindromo(teste4))