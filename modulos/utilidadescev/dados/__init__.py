def leiadinheiro(msg):
    valido = False
    while not valido:
        n = str(input(msg)).replace(',', '.').strip()
        if n.isalpha() or n == '':
            print('\033[0;31mValor inválido, tente novamente!\033[m')
        else:
            valido = True
            return float(n)

