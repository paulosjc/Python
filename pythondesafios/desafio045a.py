import random

jogador = str(input('Escolha pedra, papel ou tesoura: ')).lower().strip()

if jogador != 'pedra' and jogador != 'papel' and jogador != 'tesoura':
    print('Opção inválida! Digite novamente...')

lista = ['pedra', 'papel', 'tesoura']

computador = random.choice(lista)

if jogador == 'pedra' and computador == 'tesoura':
    print('Pedra ganha da tesoura, então você ganhou!')
elif jogador == 'tesoura' and computador == 'pedra':
    print('Pedra ganha da tesoura, então você perdeu!')
elif jogador == 'tesoura' and computador == 'papel':
    print('Tesoura ganha do papel, então você me venceu!')
elif jogador == 'papel' and computador == 'tesoura':
    print('Tesoura ganha do papel, então eu venci!')
elif jogador == 'papel' and computador == 'pedra':
    print('Papel ganha da pedra, então você me derrotou!')
elif jogador == 'pedra' and computador == 'papel':
    print('Papel ganha da pedra, então eu venci!')

if jogador == computador:
    print('Empate! O jogo deve ser reiniciado...')

