from random import randint

computador = randint(1, 11)
jogador = 0
cont = 0

while jogador != computador:
    jogador = int(input('Tente adivinhar o número em que eu pensei: '))
    cont += 1
    if jogador == computador:
        print('Você acertou, e precisou de {} tentativas.'.format(cont))