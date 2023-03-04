from time import sleep
print('-=' * 20)
print('Contagem de 1 até 10 de 1 em 1: ')
for i in range(1, 11):
    sleep(0.5)
    print(f'{i} ', end='')
    sleep(0.5)
print('FIM!')
print('-=' * 20)
print('Contagem de 10 até 0 de 2 em 2: ')
for i in range(10, -1, -2):
    sleep(0.5)
    print(f'{i} ', end='')
    sleep(0.5)
print('FIM!')
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
def contador(início, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = passo * (-1)
    if fim > início:
        for i in range(início, fim + 1, passo):
            sleep(0.5)
            print(f'{i} ', end='')
        sleep(0.5)
        print('FIM!')
        sleep(0.5)
    elif início > fim:
        for i in range(início, fim - 1, passo * (-1)):
            sleep(0.5)
            print(f'{i} ', end='')
        sleep(0.5)
        print('FIM!')
        sleep(0.5)
contador(int(input('Digite o valor inicial: ')), int(input('Digite o valor final: ')), int(input('Digite o intervalo: ')))
