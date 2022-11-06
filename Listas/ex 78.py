valores = list()
men = 0
mai = 0
for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
    if c == 0:
        men = mai = valores[c]
    else:
        if valores[c] < men:
            men = valores[c]
        elif valores[c] > mai:
            mai = valores[c]
print(valores)
print(f'O menor valor é {men} na pos: ', end='')
for i, v in enumerate(valores):
    if v == men:
        print(f'{i + 1} ')
print(f'O mai valor é {mai} na pos: ', end='')
for i, v in enumerate(valores):
    if v == mai:
        print(f'{i + 1}')
