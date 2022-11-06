def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mValor inserido é invalido\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mValor interropido pelo usuario. \033[m')
            break
        except Exception as erro:
            print(f'O erro encontrado foi {erro.__cause__}')
            continue
        else:
            return num


def leiafloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('Valor incorreto')
        except KeyboardInterrupt:
            print('O usuario decidiu não continuar')
        except Exception as erro:
            print(f'O erro encontrado foi {erro.__cause__}')
        else:
            break
    return num


n = leiaint('Digite um valor: ')
f = leiafloat('Digite um numero quebrado: ')
print(f'O valor inteiro digitado foi {n} e o real foi {f}')