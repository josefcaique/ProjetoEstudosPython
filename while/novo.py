n = int(input('Quantos termos você quer ver? '))
ant = result = 0
novo = 1
c = 0
while c != n:
    print('{} ' .format(result), end='')
    ant = novo
    novo = result
    result = novo + ant
    c += 1
print('FIM')
