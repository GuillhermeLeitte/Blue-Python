# 02 - Utilizando estruturas de repetição com variável de controle, faça um programa que receba uma string com uma frase informada pelo usuário e conte quantas vezes aparece as vogais a,e,i,o,u e mostre na tela, depois mostre na tela essa mesma frase sem nenhuma vogal.

frase = str(input('Digite uma frase (SEM ACENTOS) : ')).lower()

a = 0
e = 0
i = 0
o = 0
u = 0

for c in frase:
    if c == 'a':
        a += 1
    if c == 'e':
        e += 1
    if c == 'i':
        i += 1
    if c == 'o':
        o += 1
    if c == 'u':
        u += 1


if a != 0:
    print(f'Na sua frase têm {a} letra(s) A')
if e != 0:
    print(f'Na sua frase têm {e} letra(s) E')
if i != 0:
    print(f'Na sua frase têm {i} letra(s) I')
if o != 0:
    print(f'Na sua frase têm {o} letra(s) O')
if u != 0:
    print(f'Na sua frase têm {u} letra(s) U')

frase = frase.replace('a', '')
frase = frase.replace('e', '')
frase = frase.replace('i', '')
frase = frase.replace('o', '')
frase = frase.replace('u', '')

print(f'Sua frase sem as vogais é: {frase}')
