
expr = str(input('Digite a expresssão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
         if len(pilha) > 0:
             pilha.pop()
         else:
             pilha.append(')')
             break
if len(pilha) == 0:
    print('Sua expressão está correta')
else:
    print('Sua expressão está errada')
print(pilha)


