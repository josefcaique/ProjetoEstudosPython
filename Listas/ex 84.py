pessoas = []
mais_pes = []
mais_lev = []
c = 0
while True:
    pessoas.append(str(input('digite o nome: ')))
    pessoas.append(float(input('Digite o peso: ')))
    mais_lev.append(pessoas[:])
    mais_pes.append(pessoas[:])
    pessoas.clear()
    c += 1
    r = str(input('Você deseja continuar [S/N]? ')).strip().upper()[0]
    if r in 'N':
        break
for cont, v in enumerate(mais_lev):
    if v[1] >= 100:
        del(mais_lev[cont])
for a, b in enumerate(mais_pes):
    if b[1] < 100:
        del(mais_pes[a])
print(f'foram cadastrada  {c} pessoas')
print(f'As pessoas mais leve foram {mais_lev}')
print(f'As pessoas mais pesadas foram {mais_pes}')
