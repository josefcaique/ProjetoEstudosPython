from random import randint
tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
for n in tupla:
    print(f'{n} ', end='')
print(f'\nO maior valor é {max(tupla)} \nO menor valor é {min(tupla)}')
