from time import sleep

def contador(início, fim, passo):
    if fim > início:
        for i in range(início, fim + 1, passo):
            sleep(0.5)
            print(f' {i}', end='')
        sleep(0.5)
        print(' FIM!')
        sleep(0.5)
    elif início > fim:
        for i in range(início, fim + 1, passo * (-1)):
            sleep(0.5)
            print(f' {i}', end='')
        sleep(0.5)
        print(' FIM!')
        sleep(0.5)

contador(int(input('Digite o valor inicial: ')), int(input('Digite o valor final: ')), int(input('Digite o intervalo: ')))
