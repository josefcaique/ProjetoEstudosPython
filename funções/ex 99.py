from time import sleep
def maior(*n):
    mai = 0
    print('==' * 30)
    print('Analisando os valores passados...')
    for c, num in enumerate(n):
        print(num, end=' ')
        sleep(0.75)
        if c == 0 or num > mai:
            mai = num
    print(f'Foram informados {len(n)} valores ao todo')
    print(f'O maior valor informado foi {mai}')
    print('==' * 30)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
