from time import sleep

def maior(* num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    tam = len(num)
    if tam == 0:
        print(f'Foram informados 0 valores ao todo.')
        print(f'O maior valor informado foi 0.')
    else:
        for i in num:
            print(f'{i} ', end='')
            sleep(0.5)
        print(f'Foram informados {tam} valores ao todo.')
        print(f'O maior valor informado foi {max(num)}.')
maior(2, 5, 1, 10)
maior(5, 2, 8, 34)
maior(3, 6, 10, 24, 14, 19)
maior()
