def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('\033[32mMENU PRINCIPAL\033[m')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('Sua opção: ')
    return opc


def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mValor inválido, tente novamente!\033[m')
        except KeyboardInterrupt:
            print('\033[31mO usuário decidiu não prosseguir\033[m')
            break
        except Exception as erro:
            print(f'\033[31mO erro encontrado foi {erro.__cause__}\033[m')
        else:
            return num
