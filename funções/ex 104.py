def leiaint(txt):
    ok = False
    while True:
        num = str(input(txt))
        if num.isnumeric():
            num = float(num)
        else:
            print('\033[0;31mErro, digite um número válido.\033[m')
        if ok:
            break
    return num


n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}')
