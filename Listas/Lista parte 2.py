    #teste = list()
    #teste.append('Gustavo')
    #teste.append(40)
    #galera = list()
    #galera.append(teste[:])
    #teste[0] = 'Maria'
    #teste[1] = 22
    #print(teste)
   #print(galera)

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[0])
print(galera[2][1])
print(galera[3][0])

for pes in galera:
    print(f'{pes[0]} tem {pes[1]} anos de idade')

galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Digite um nome: ')))
    dado.append(int(input('digite a idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
    else:
        print(f'{p[0]} é menor de idade')

