# EXERCÍCIO 7.3
# Escreva uma função recursiva que diga se uma frase é um palíndromo. Não esqueça de ignorar ou apagar os espaços antes de comparar as letras.
# Ex: “A mala nada na lama”, “a base do teto desaba”.

def palindromo_frase(frase: str):
    frase = frase.replace(" ", "").lower()
    if len(frase) <= 1:
        return True
    elif frase[0] == frase[-1]:
        return palindromo_frase(frase[1:-1])
    else:
        return False


teste1 = "A mala nada na lama"
teste2 = "a base do teto desaba"

print(palindromo_frase(teste1))
print(palindromo_frase(teste2))