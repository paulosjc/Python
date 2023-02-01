import random

n = random.randint(0, 5)

num = int(input('Digite um número entre 0 e 5: '))

if n == num:
    print('Parabéns! Você acertou o número!')
else:
    print('Você não acertou o número...')

print('O valor sorteado foi: {}'.format(n))
print('O palpite foi: {}'.format(num))

