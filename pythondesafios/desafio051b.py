print('\033[33m=\033[m' * 50)
print('\033[34m          10 Primeiros termos de uma P.A.\033[m')
print('\033[33m=\033[m' * 50)
n = 10
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da P.A.: '))
décimo = p + (n - 1) * r

for c in range(p, décimo + 1, r):
    print(c, end = ' ➡️ ')
print('Fim')


