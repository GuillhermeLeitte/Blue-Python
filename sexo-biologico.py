""" #02 - Faça um programa que leia o sexo biológico de uma pessoa, mas
só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação
novamente até ter um valor correto. """

sexobio = str(input('Qual seu sexo biológico: [M/F]')).upper()

while sexobio not in 'MF':
    print('Você tem que digitar [M ou F]')
    sexobio = str(input('Qual seu sexo biológico: [M/F]')).upper()
print(f'{sexobio} registrado')
