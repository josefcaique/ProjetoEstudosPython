num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
num.pop()
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
    print(num)
print(f'Essa lista tem {len(num)} elementos')

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for pos, v in enumerate(valores):
    print(f'Os valores são {v} na posição {pos + 1}')
