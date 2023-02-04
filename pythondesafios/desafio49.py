print('\033[33m-=-' * 20)
print('\033[34m     Programa que calcula a tabuada de qualquer número\033[m')
print('\033[33m-=-\033[m' * 20)
n = int(input('\033[32mDigite um número inteiro qualquer para ver sua tabuada: \033[m'))

for c in range(1, 11):
    print('{} x {:2} = {:3}'.format(n, c, n * c))