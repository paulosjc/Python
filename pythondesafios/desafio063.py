print('\033[33m-=-\033[m' * 10)
print('\033[34m     Série de Fibonacci\033[m')
print('\033[33m-=-\033[m' * 10)

n = int(input('Quantos termos você quer mostrar da sequência de Fibonacci? '))
print('~' * 60)
t1 = 0
t2 = 1

print('{} ➡️ {} ➡️ '.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('{} ➡️ '.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('Fim')
print('~' * 60)