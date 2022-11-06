vp = float(input('Digite o valor do produto: '))
opc = str(input('''Sel a opção:
a vista
cartao
parcelado 2x 
parcelado + '''))
if opc == 'a vista':
    vp1 = vp - (vp * 0.1)
    print(vp1)
elif opc == 'cartao':
    vp1 = vp - (vp * 0.05)
    print(vp1)
elif opc == 'parcelado 2x':
    vp1 = vp
    print(vp1)
elif opc == 'parcelado +':
    vp1 = vp + (vp * 0.2)
    print(vp1)
else:
    print("Valor inválido")