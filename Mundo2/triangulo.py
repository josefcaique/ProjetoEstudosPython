p = float(input('Digite o seu peso: '))
a = float(input('Digite a sua altura: '))
imc = p / (a * a)
if imc < 18.5:
    print('Está abaixo do peso')
elif  imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('obesidade')
else:
    print('Obesidade mórbida')