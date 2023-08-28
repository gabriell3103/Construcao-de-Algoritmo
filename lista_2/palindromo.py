def verificar_palindromo(string):
    string_invertida = string[::-1]
    if string_invertida == string:
        return True
    return False

string = 'tut'
verificar_palindromo(string)