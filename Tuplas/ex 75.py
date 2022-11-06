n = (int(input('Digite um número: ')),
     int(input('Digite um número: ')),
     int(input('Digite um número: ')),
     int(input('Digite um número: ')))
print(f'Você digitou {n}')
if 9 in n:
    print(f'\nO número 9 aparece {n.count(9)} vez vezes')
else:
    print(f'\nO número 9 aparece nenhuma vez')
if 3 in n:
    print(f'O numero 3 aparece na {n.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi encontrado')
print('Os números pares são: ', end='')
for count in n:
    if count % 2 == 0:
        print(count, end=' ')
