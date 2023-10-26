def como_funciona_o_enumerate(lista: list):
    contador = 1
    print('Sem enumerate')
    for item in lista:
        print(f'{contador} - {item}')
        contador += 1
    print(10 * '-=')
    print('Com enumerate')
    for indice, item in enumerate(lista): # No enumerate, a primeria variavel é o indice e o segundo o valor.
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