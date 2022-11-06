lista = []
while True:
    nome = str(input('Digite o nome do aluno: '))
    n1 = float(input('Digite a nota 1: '))
    n2 = float(input('Digite a nota 2: '))
    media = (n1 + n2) / 2
    lista.append([nome, [n1, n2], media])
    r = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if r in 'Nn':
        break
print('=-' * 20)
print(f'No.      NOME   MEDIA')
print('=-' * 20)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('=' * 40)
    opc = int(input('Mostrar nota de qual aluno? (999 para cancelar) '))
    for b in lista:
        if opc == 999:
            break
    if opc <= len(lista) - 1:
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')
