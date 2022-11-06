from time import sleep

def contador(a, b, c):
    cont = a
    if c == 0:
        c = 1
    if c < 0:
        c *= -1
    print(f'Contagem de {a} até {b} de {c} em {c}')
    if a < b:
        while cont <= b:
            print(cont, end=' ')
            cont += c
            sleep(0.5)
    elif a > b:
        while cont >= b:
            print(cont, end=' ')
            cont -= c
            sleep(0.5)
    print('FIM!')
contador(1, 10, 1)
contador(10, 1, -2)
print('Faça a seu própio contador!')
a = int(input('Digite o inicio: '))
b = int(input('Digite o fim: '))
c = int(input(('Digite o passo: ')))
contador(a, b, c)
