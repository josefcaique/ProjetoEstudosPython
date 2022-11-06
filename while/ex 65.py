num = int(input('Digite um valor inteiro: '))
s = mai = men = num
c = 1
res = str(input('Você deseja continuar [S/N]? ')).upper().strip()[0]
while res in 'Ss':
    num = int(input('Digite um valor inteiro: '))
    s += num
    c += 1
    if num > mai:
        mai = num
    elif num < men:
        men = num
    res = str(input('Você deseja continuar [S/N]? ')).upper()
print('A media entre os valores é {:.2f} '.format(s/c), end='')
print(f'e o maior valor é {mai} e o menor {men}')
