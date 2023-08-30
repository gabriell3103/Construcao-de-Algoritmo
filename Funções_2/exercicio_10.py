def encontrar_substring(string, substring):
    if substring in string:
        return True
    else:
        return False

string = 'passei'
sub = 'assei'
print(encontrar_substring(string, sub))