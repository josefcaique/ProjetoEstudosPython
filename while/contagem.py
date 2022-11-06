n = s = c = 0
while n != 999:
    n = int(input('Digite um número (999 para parar o programa): '))
    if n != 999:
        c += 1
        s += n
print('Você tentou {} vezes e a soma dos valores foi {}' .format(c, s))