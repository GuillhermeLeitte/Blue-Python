# 08 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade, com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar.


cadastro = dict()

nome = input('Digite seu nome: ')
anoNascimento = int(
    input('Digite o ano do seu nascimento em 4 dígitos [ex: 1991]: '))
ctps = int(input('Qual o número da sua Carteira de trabalho? : ').replace(
    ',', '.').replace('.', ''))

anoAtual = int(input('Em que ano estamos? em 4 dígitos [ex: 2021]:'))


cadastro['nome'] = nome
cadastro['idade'] = anoAtual - anoNascimento
cadastro['ctps'] = ctps

if ctps != 0:
    anoContratacao = int(input('Em que ano foi a contratação? : '))
    salário = float(input('Seu salário: '))
    cadastro['Ano de contratação'] = anoContratacao
    cadastro['Salário'] = salário
    cadastro['Idade de aposentadoria'] = (anoContratacao - anoNascimento) + 35
print(cadastro)
