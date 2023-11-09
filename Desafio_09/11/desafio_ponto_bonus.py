import unittest

def herdeiros(Familia: list[dict]) -> str:
    result = [Familia[0]['nome']]

    def buscar_herdeiro(pai):
        herdeiros = [individuo['nome'] for individuo in Familia if individuo['pai'] == pai]
        for filho in herdeiros:
            result.append(filho)
            buscar_herdeiro(filho)

    buscar_herdeiro(Familia[0]['nome'])
    return ' -> '.join(result)

minhaFamilia = [
    {'nome': 'Eduardo', 'pai': None},
    {'nome': 'Lucas', 'pai': 'Eduardo'},
    {'nome': 'Pedro', 'pai': 'Lucas'},
    {'nome': 'João', 'pai': 'Pedro'}
]

def test_1():
    assert herdeiros(minhaFamilia) == 'Eduardo -> Lucas -> Pedro -> João'
    print('OK - 1')
def test_2():
    assert herdeiros(minhaFamilia[0]) == 'Eduardo'
    print('OK - 2')
def test_3():
    assert herdeiros(minhaFamilia[0:3]) == 'Eduardo -> Lucas -> Pedro'
    print('OK - 3')
def test_4():
    assert herdeiros(minhaFamilia[1:]) == 'Lucas -> Pedro -> João'
    print('OK - 4')

if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()