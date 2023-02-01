import random
from time import sleep

print('\033[33m-=-\033[m' * 20)
print('\033[34mEscolha uma dentre as seguintes opções:\033[m')
print('''
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
''')
print('\033[33m-=-\033[m' * 20)
entrada = int(input('Escolha sua opção: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
lista = ['Pedra', 'Papel', 'Tesoura']
computador = random.randint(0, 2)
jogador = entrada - 1

if jogador != 0 and jogador != 1 and jogador != 2:
    print('Opção inválida! Digite novamente...')

if jogador == 0 and computador == 2:
    print('{} ganha de {}, então você ganhou!'.format(lista[0], lista[2]))
elif jogador == 2 and computador == 0:
    print('{} perde para a {}, então eu ganhei!'.format(lista[2], lista[0]))
elif jogador == 2 and computador == 1:
    print('{} ganha do {}, então você me venceu!'.format(lista[2], lista[1]))
elif jogador == 1 and computador == 2:
    print('{} ganha do {}, então eu venci!'.format(lista[1], lista[2]))
elif jogador == 1 and computador == 0:
    print('{} ganha de {}, então você me derrotou!'.format(lista[1], lista[0]))
elif jogador == 0 and computador == 1:
    print('{} ganha da {}, então eu venci!'.format(lista[1], lista[0]))

if jogador == computador:
    print('Empate! O jogo deve ser reiniciado...')

