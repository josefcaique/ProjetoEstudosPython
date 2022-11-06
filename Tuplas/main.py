lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# soluções diferentes
for comida in lanche:
    print(f'vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu comi {lanche[cont]} na posição {cont + 1}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

lanche.index('Hamburguer')
max(lanche)
min(lanche)
print(sorted(lanche))
