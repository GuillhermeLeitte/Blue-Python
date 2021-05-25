""" 1. Crie um código em Python que pede qual tabuada o usuário quer ver, em
seguida imprima essa tabuada. """


def tabuada(x):
    for c in range(1, 11):
        print(f'{x} x {c:2} = {c*x}')


tabuada(int(input('Digite o número que quer ver a sua tabuada: ')))
