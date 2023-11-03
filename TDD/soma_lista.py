import unittest

def soma_lista(numeros):
    n = numeros.pop()
    if len(numeros) == 0:
        return n
    else:
        return n + soma_lista(numeros)
    
def test_1_soma_lista():
    assert soma_lista([1, 2, 3]) == 6
    print('OK - soma certo 01')

def test_2_soma_lista():
    assert soma_lista([5, 7, 9, 11]) == 32
    print('OK - soma certo 02')

def test_3_soma_lista():
    assert soma_lista([]) == 0
    print('OK - soma certo 03')

if __name__ == '__main__':
    test_1_soma_lista()
    test_2_soma_lista()
    test_3_soma_lista()