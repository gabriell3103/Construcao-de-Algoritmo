def como_funciona_o_enumerate(lista: list):
    contador = 1
    for item in lista:
        print(f'{contador} - {item}')
        contador += 1
    print(10 * '-=')
    for indice, item in enumerate(lista):
        print(f'{indice + 1} - {item}')

frutas = [
    'laranja',
    'goiaba',
    'pera',
    'maça',
    'uva',
    'morango',
    'jaca',
    'umbu'
]

como_funciona_o_enumerate(frutas)