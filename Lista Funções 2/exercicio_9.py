def verificar_anagrama(string1: str, string2: str):
    string_nova1 = sorted(string1)
    string_nova2 = sorted(string2)

    if string_nova1 == string_nova2:
        return True
    return False

string1 = 'alo'
string2 = 'ola'
print(verificar_anagrama(string1, string2))