from random import randint
from time import sleep

print('-' * 30)
print(f'{"Jogo da Mega Sena":^30}')
print('-' * 30)
jogo = []
jogos = []
num = []

n = int(input('Quantos jogos você quer que eu sorteie? '))

for i in range(0, n):
    for i in range(0, 6):
        v = randint(1, 60)
        if v not in num:
            num.append(v)
    if len(num) < 6:
        p = randint(1, 60)
        if p not in num:
            num.append(p)
    num.sort()
    jogo.append(num[:])
    num.clear()

print(jogo)

print('-=' * 3, end='')
print(f' SORTEANDO {n} JOGOS ', end='')
print('-=' * 3)
for i in range(0, n):
    sleep(2)
    print(f'{i + 1}º jogo: {jogo[i]}')
print('-=' * 5, end='')
print(f'{" < BOA SORTE! > "}', end='')
print('-=' * 5)
