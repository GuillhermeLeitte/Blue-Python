# 01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:
# A soma deles;
# A multiplicação entre eles;
# A divisão inteira deles;
# Mostre na tela qual é o maior;
# Verifique se o resultado da soma é par ou impar e mostre na tela;
# Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre o resultado na tela. Se não, mostre que a multiplicação não foi maior que 40.

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

soma = num1+num2
print(f'A soma entre {num1} e {num2} é: {soma}')

mult = num1*num2
print(f'A multiplicação entre {num1} e {num2} é: {mult}')

if num1 >= num2:
    div1 = num1//num2
    print(f'A divisão entre {num1} e {num2} é: {div1}')
else:
    div1 = num2 // num1
    print(f'A divisão entre {num2} e {num1} é: {div1}')

if num1 > num2:
    print(f'O {num1} é o maior número')
else:
    print(f'O {num2} é o maior número')

if soma % 2 == 0:
    print(f'A soma entre {num1} e {num2} é: {soma} que é par')
else:
    print(f'A soma entre {num1} e {num2} é: {soma} que é ímpar')

if mult > 40:
    mult //= div1
    print(
        f'A divisão entre o resultado da multiplicação e o produto  divisão do {num1}/{num2} é de :{mult}')
else:
    print(f'A multiplicação entre os dois números foi menor que 40 \n')

print('--'*40)
print('Fim do programa')

