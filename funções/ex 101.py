def voto(ano):
    from datetime import datetime
    ida = datetime.now().year - ano
    if 17 <= ida < 18 or ida > 65:
        vot = 'OPCIONAL'
    elif ida >= 18:
        vot = 'OBRIGATÓRIO'
    else:
        vot = 'NEGADO'
    return f'com {ida} ano o voto é: {vot}'


nas = int(input('Em que ano você nasceu? '))
print(voto(nas))
