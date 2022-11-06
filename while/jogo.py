from random import randint
print('=-'*10)
print('Jogo da advinhação')
print('=-'*10)
n = int(input('\033[31m Estou pensando em um numéro de 1 a 10, tente adivinhar: \033[m'))
pc = randint(1, 10)
t = 1
if n == pc:
    print('Parabéns, você acertou na {}º tentativa!!!'.format(t))

while pc != n:
    if n > pc:
        print('menos... Tente novamente: ')
    else:
        print('mais... tente novamente: ')
    n = int(input('Qual o seu palpite: '))
    t += 1
    if n == pc:
        print('Parabéns, você acertou na {}º tentativa!!!'.format(t))