lista = []
cont5 = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    r = str(input('Você deseja continuar [S/N]? ')).strip().upper()[0]
    if r not in 'Ss':
        print('Programa enceraddo!')
        break
print(f'Foram adicionados {len(lista)} números')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print('O valor 5 está na lista!')
else:
    print('Não foi possível encontrar o 5!')
