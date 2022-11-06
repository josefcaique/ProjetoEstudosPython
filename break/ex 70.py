print('Loja Super Baratão')
men = c = t = count = 0
nb = ' '
while True:
    nome = str(input('Qual o nome do produto: '))
    preco = float(input('Preço: '))
    t += preco
    count += 1
    if preco > 1000:
        c += 1
    if count == 1 or preco < men:
        men = preco
        nb = nome
    con = ' '
    while con not in 'SN':
        con = str(input('Deseja continuar [S/N]')).upper().strip()[0]
    if con != 'S':
        break
print(f'O total gasto na compra é {t}')
print(f'{c} custam mais que 1000 reais')
print(f'O produto mais barato é {nb} no valor de {men}')
