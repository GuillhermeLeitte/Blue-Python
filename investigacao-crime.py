#06 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
   # "Telefonou para a vítima?"
   # "Esteve no local do crime?"
   # "Mora perto da vítima?"
   # "Devia para a vítima?"
   # "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
   # Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
   # Entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
   # Caso contrário, ele será classificado como "Inocente".


acusado = str(input('Qual seu nome? '))

a = input('Telefonou para a vítima? \n Responda  [S/N]: ').strip().upper()[0]
b = input('Esteve no local do crime? \n Responda [S/N]: ').strip().upper()[0]
c = input('Mora perto da vítima? \n Responda [S/N]: ').strip().upper()[0]
d = input('Devia para a vítima?\n Responda  [S/N]: ').strip().upper()[0]
e = input('Já trabalhou com a vítima?\n Responda [S/N]: ').strip().upper()[0]

resp = [a, b, c, d, e]

resultado = 0 

for c in resp: 
    if c == 'S': 
        resultado += 1 

if resultado == 2: 
    print(f'{acusado} você é Suspeito(a)')

elif resultado >= 3 and resultado <= 4:
    print(f'{acusado} você é Cumplice')

elif resultado == 5:
    print(f'{acusado} você é Assassino(a)')

else:
    print(f'{acusado} você é Inocente')