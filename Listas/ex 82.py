num = []
pares = []
impares = []
while True:
    num.append(int(input('Digite um valor: ')))
    r = str(input('deseja continuar [S/N]? ')).upper().strip()[0]
    if r in 'N':
        break
for i, c in enumerate(num):
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)
print(f'a lista de números é {num}')
print(f'A lista de pares é {pares}')
print(f' A lista de impares é {impares}')
