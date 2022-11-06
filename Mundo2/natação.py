ida = int(input('Digite a idade do atleta: '))
if ida <= 9:
    print('Você é nadador Mirim')
elif ida <= 14:
    print('Você é nadador Infantil')
elif ida <= 19:
    print('Você é nadador Junior')
elif ida == 25:
    print('Você é Sênior')
else:
    print('Você é Master')