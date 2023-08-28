def contador_vogais(string):
    vogais = 0
    for i in string:
        if i == 'a'or i == 'A':
            vogais += 1
        elif i == 'e' or i == 'E':
            vogais += 1
        elif i == 'i' or i == 'I':
            vogais += 1
        elif i == 'o'or i == 'O':
            vogais += 1
        elif i == 'u' or i == 'U':
            vogais += 1
    return print(vogais)

def vogais_2(string: str):
    contador = 0
    vogais = ['a', 'e', 'i', 'o', 'u']
    for letra in string.lower:
        if letra in vogais:
            contador += 1
    
    return contador
 
string = 'arroz'
vogais_2(string)