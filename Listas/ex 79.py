lista = []
while True:
    n = int(input('digite um valor: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Valor já adicionado, tente outro!')
    r = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if r in 'Nn':
        print('Programa encerrado!!')
        break
lista.sort()
print(lista)
