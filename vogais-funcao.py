# 05 - Refatore o exercício 2, para que uma função receba a frase, faça todo o tratamento necessário e retorne o resultado. Depois mostre na tela o resultado e a quantidade de letras foram retiradas da frase original.

def texto():
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

    soma = a + e + i + o + u
    print(f'A quantidade de letras retiradas da frase foi de :{soma}')

    frase = frase.replace('a', '')
    frase = frase.replace('e', '')
    frase = frase.replace('i', '')
    frase = frase.replace('o', '')
    frase = frase.replace('u', '')

    print(f'Sua frase sem as vogais é: {frase}')


texto()
