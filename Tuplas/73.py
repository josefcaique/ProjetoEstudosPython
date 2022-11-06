brasileirao = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense',
               'América_MG', 'Atético_GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá',
               'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')
print(f'Os primeiros colocados do Brasileiro são\n {brasileirao[:5]}')
print(f'Os ultimos colocados foram {brasileirao[16:]}')
print(sorted(brasileirao))
for cont in range(0, len(brasileirao)):
    if brasileirao[cont] == 'Chapecoense':
        print(f'O {brasileirao[cont]} está na {cont + 1}º colocação')
