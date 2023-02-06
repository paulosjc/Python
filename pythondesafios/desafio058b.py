from random import randint

computador = randint(1, 10)
print('Sou o seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar?')
acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente de novo.')
        elif jogador > computador:
            print('Menos...Tente de novo.')
print('Você acertou com {} tentativas. Parabéns!'.format(palpites))
