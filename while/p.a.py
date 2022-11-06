pt = int(input('Qual o primeiro termo: '))
r = int(input('qual a razão: '))
termo = pt
q = 10
s = 0
c = 1
while q != 0:
    c = 1
    s = s + q
    while c <= q:
        print('{} '.format(termo), end='')
        c += 1
        termo += r
    print('Pausa')
    q = int(input('Quantos termos você quer ver a mais? '))
print('Progressão finalizada com {} termos mostrados' . format(s))
