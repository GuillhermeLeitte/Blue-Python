# 03 - Utilizando estruturas de repetição com teste lógico, faça um programa que peça uma senha para iniciar seu processamento, só deixe o usuário continuar se a senha estiver correta, após entrar dê boas vindas a seu usuário e apresente a ele o jogo da advinhação, onde o computador vai “pensar” em um número entre 0 e 10. O jogador vai tentar adivinhar qual número foi escolhido até acertar, a cada palpite do usuário diga a ele se o número escolhido pelo computador é maior ou menor ao que ele palpitou, no final mostre quantos palpites foram necessários para vencer.

from random import randint
senha = int(input('Digite a senha para entrar: '))

while senha != 1095:
    print('Senha incorreta \n Tente novamente: \n')
    senha = int(input('Digite a senha para entrar: '))
    if senha == 1095:
        print('\n Iniciando sistema...')

print('--'*60)

print(' Seja bem vindo!! ')
print(' \n  Jogo da Adivinhação')

print('Pensei em um número será que você descobre??:')


usuario = int(input('Adivinhe o número escolhido entre [0 e 10] :'))

computador = randint(0, 10)

tentativas = 1

while usuario != computador:
    print('Errou!! ')
    tentativas += 1
    print("-"*60)

    if usuario > computador:
        print('Dica: é um número menor !! \n Tente novamente...')

        usuario = int(input('Adivinhe o número escolhido entre [0 e 10] :'))

    if usuario < computador:
        print('Dica: é um número maior !! \n Tente novamente...')

        usuario = int(input('Adivinhe o número escolhido entre [0 e 10] :'))

    elif usuario == computador:    
        print('Acertou!!')
        print(f'Parabéns!!! \n Você precisou de {tentativas} tentativas para acertar.')
