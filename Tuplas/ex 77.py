tupla = ('bola', 'cavalo', 'agua', 'maca', 'gratis', 'estudar', 'aprender', 'myl', 'fggfg')
for p in tupla:
    print(f'\n Na palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
