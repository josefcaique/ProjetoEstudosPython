cidade = str(input('Digite a sua cidade: ')).upper()
dividido = cidade.split()
res = 'SANTO' in dividido[0]
print(res)
