def fatorial(n=1):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f


num = int(input('Digite um valor para faotriar: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')


def par(a=0):
    if a % 2 == 0:
        return True
    else:
        return False


print(par(5))
