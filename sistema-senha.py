""" #01 - Escreva um programa que pede a senha ao usuário, e só sai do
looping quando digitarem corretamente a senha: """

senha = int(input('Digite a senha; '))

while senha != 1095:
    print('Senha incorreta. \n Digite nova senha:')
    senha = int(input('Digite a senha: '))
    if senha == 1095:
        print('Senha correta, Abrindo sistema...')


""" n = 1
while n != 0: # O while é um laço com condição de parada, ENQUANTO o n for diferente de zero, faça...
   n = int(input('Digite um valor: '))
print('Fim') """
