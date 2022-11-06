print('CAIXA ELETRÔNICO')
n50 = n20 = n10 = n1 = 0
c = 1
res = 0
val = int(input('Qual o valor a ser sacado? '))
while True:
    if val >= 50:
        n50 = val // 50
        val = val % 50
        print(f'Total de {n50} cédulas de R$50')
    if val >= 20:
        n20 = val // 20
        val = val % 20
        print(f'Total de {n20} cédulas de R$20')
    if val >= 10:
        n10 = val // 10
        val = val % 10
        print(f'Total de {n10} cédulas de R$10')
    if val >= 1:
        n1 = val // 1
        val = val % 1
        print(f'Total de {n1} cédulas de R$1')
    if val == 0:
        break