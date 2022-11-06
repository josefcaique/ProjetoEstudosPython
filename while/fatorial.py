n = int(input('Digite o valor que deseja fatoriar: '))
f = 1
print('calculando {}! =' .format(n), end='')
while n > 0:
    f = f * n
    n = n - 1
print(f)
