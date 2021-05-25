""" #01 - Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes
informações:
a) tamanho da lista.
b) maior valor da lista.
c) menor valor da lista.
d) soma de todos os elementos da lista.
e) lista em ordem crescente.
f) lista em ordem decrescente. """

l = [5, 7, 2, 9, 4, 1, 3]
l.sort()


print(f' O tamaho da lista é de :{len(l)}')
print(f'O maior valor da lista é: {max(l)}')
print(f'O menor valor da lista é: {min(l)}')
print(f'A soma dos valores da lista é: {sum(l)}')
print(f'A ordem crescente dos valores da lista é: {l}')

l.reverse()
print(f'A ordem decrescente dos valores da lista é: {l}')
