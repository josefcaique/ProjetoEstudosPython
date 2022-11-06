c = 0
m = 0
mai = 0
sel = 0
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
print('=-=-=-=-=-= Menu Principal =-=-=-=-=-=-=')
while sel != 5:
    sel = int(input('Selecione o que você deseja: \n'
                    '[1]Somar \n'
                    '[2]Multiplicar \n'
                    '[3]Maior \n'
                    '[4]Novos números \n'
                    '[5]Sair do programa \n'))
    if sel == 1:
        c = n1 + n2
        print('O valor da soma é: {} \n' .format(c))

    if sel == 2:
        m = n1 * n2
        print('O valor da multiplicação é {} \n' .format(m))

    if sel == 3:
        if n1 > n2:
            mai = n1
            print(f'O maoir é {mai} \n')
        elif n2 > n1:
            mai = n2
            print(f'O maior é {mai} \n')
        else:
            print('Os valores são iguais \n')

    if sel == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))




print('Programa encerrado')





