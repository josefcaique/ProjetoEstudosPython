imovel = int(input('Qual o valor do imóvel comprar?'))
sal = int(input('Qual o seu salario? '))
ano = int(input('Em quantos anos você pretende pagar? '))
p = imovel // (ano*12)
if p > 0.3 * sal:
    print('Infelizmente não foi possivel realizar a comprar')
else:
    print('Compra realizada com sucesso')
