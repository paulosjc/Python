from random import randint
from time import sleep
jogador = computador = cont = res = 0

while True:
    computador = randint(0, 6)
    jogador = int(input('Entre com um valor entre 0 e 5: '))
    if jogador not in range(0, 6):
        print('Número não permitido. Digite de novo...')
    else:
        soma = computador + jogador
        if soma % 2 == 0:
            r = 0
        else:
            r = 1
        res = int(input('Par ou ímpar? [0/1] '))
        if res != 0 and res != 1:
            print('Resposta inválida. Digite novamente...')
        if res == 0 or res == 1:
            if res == r:
                cont += 1
                print('Acertou! Continue...')
            if res != r:
                print('Ah! Ganhei!')
                sleep(1)
                print('Finalizando...')
                sleep(1)
                break
print(f'Você acertou {cont} vezes consecutivas.')
