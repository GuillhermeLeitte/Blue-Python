""" #02 - Utilizando listas, faça um programa que faça 5 perguntas para uma pessoa sobre um
crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como
"Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será
classificado como "Inocente". """

soma = 0

print('Responda SIM ou NÃO')
a = str(input('Telefonou para a vitima?')).lower()
if a == 'sim':
    soma += 1

b = str(input('Esteve no local do crime?')).lower()
if b == 'sim':
    soma += 1

c = str(input('Mora perto da vitima?')).lower()
if c == 'sim':
    soma += 1

d = str(input('Devia para a vitima?')).lower()
if d == 'sim':
    soma += 1

e = str(input('Já trabalhou com a vitima?')).lower()

if e == 'sim':
    soma += 1

if soma == 0 or soma < 2:
    print('Inocente')

if soma == 2:
    print("Suspeita")

if soma == 3 or soma == 4:
    print("Cúmplice")

if soma == 5:
    print("Assassino")


""" lista = [a, b, c, d, e]
print(lista) """
