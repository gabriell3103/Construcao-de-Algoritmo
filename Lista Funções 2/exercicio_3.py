def verificar_palindromo(string):
    string_invertida = string[::-1]
    if string_invertida == string:
        return True, print('Esta palavra é palindroma!')
    return False, print('Esta palavra não é palindroma!')

string = 'tut'
verificar_palindromo(string)