import random
joken = str(input('Jogador escolha entre pedra, papel, tesoura '))
lista = ['pedra', 'papel', 'tesoura']
pc = random.choices(lista)

if joken == 'pedra':
    if pc == 'pedra':
        print('Empate -_-')
    elif pc == 'papel':
        print('Você perdeu :(')
    elif pc == 'tesoura':
        print('Você ganhou')

elif joken == 'papel':
    if pc == 'papel':
        print('Empate')
    elif pc  == 'tesoura':
        print('Voce perdeu')
    elif pc == 'pedra':
        print('voce ganhou')
