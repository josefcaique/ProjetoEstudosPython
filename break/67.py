while True:
    c = 1
    print('-' * 30)
    n = int(input('Digite um valor para a tabuada: '))
    print('-' * 30)
    if n < 0:
        break
    while c <= 10:
        print(f'{n} X {c} = {n * c}')
        c += 1
print('Tabuada finalizada, volte sempre!')
