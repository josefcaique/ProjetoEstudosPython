n = []
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    print(len(n))
    if c == 0 or num > n[-1]:
        n.append(num)
        print('adicionado no Final da lista')
    else:
        pos = 0
        while pos < len(n):
            if num <= n[pos]:
                n.insert(pos, num)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print(n)