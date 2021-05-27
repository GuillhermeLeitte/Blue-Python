# 07 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.


valores = [[], []]

for c in range(1, 8):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)

valores[0].sort()

valores[1].sort()

print(f'''
Pares {valores[0]}
Impares {valores[1]}
''')
