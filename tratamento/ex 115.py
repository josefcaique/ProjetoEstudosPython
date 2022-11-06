from time import sleep
from Interface import *
from arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criararquivo(arq)
else:
    print('Arquivo encontrado com sucesso!')

while True:
    resp = menu(['Listar Pessoas', 'Cadastrar novas peossoa', 'Sair do Sistema'])
    if resp == 1:
        # opção de listar o conteudo do arquivo
        lerarquivo(arq)
    elif resp == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mNúmero inválido\033[m')
    sleep(1)
