from time import sleep
c = ('\033[m',
     '\033[0;41m',
     '\033[1;42m',
     '\033[1;44m',
     '\033[1;107m')


def tam(txt, cor=0):
    tamanho = len(txt) + 4
    print(c[cor], end='')
    print('~' * tamanho)
    print(f'  {txt}')
    print('~' * tamanho)
    print(c[0], end='')
    sleep(1)


def manual(resp):
    tam(f'Acessando o manual do comando "{resp}"', 3)
    print(c[4], end='')
    help(resp)
    print(c[4], end='')
    sleep(2)


while True:
    tam('SISTEMADE AJUDA pyHELP', 2)
    r = str(input('Função ou biblioteca > ')).strip()
    if r.upper() == 'FIM':
        tam('Até logo', 1)
        break
    manual(r)
