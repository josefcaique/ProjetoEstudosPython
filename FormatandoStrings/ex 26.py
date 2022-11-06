frase = str(input('Digite uma frase: ')).upper()
print(f'Foi possível achar a letra a {frase.count("A")} vezes')
print(f'Ela aparece a primeira vez na posição {frase.find("A") + 1}')
print(f'A ultima vez que ela aparece é na pos {frase.rfind("A") + 1}')
