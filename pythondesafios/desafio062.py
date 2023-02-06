print('\033[33m=\033[m' * 50)
print('\033[34m          10 Primeiros termos de uma P.A.\033[m')
print('\033[33m=\033[m' * 50)

p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da P.A.: '))
termo = p
c = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while c <= total:
        print('{} ➡️ '.format(termo), end='')
        termo += r
        c += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Fim')
print('Progressão finalizada com {} termos'.format(total))
