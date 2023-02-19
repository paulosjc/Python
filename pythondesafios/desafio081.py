num = []
cont = 0

while True:
    num.append(int(input('Digite um número: ')))
    cont += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

if 5 in num:
    print('O número 5 está na lista!')
else:
    print('O número 5 não está na lista...')

print(num)
print(sorted(num, reverse=True))
print(cont)
print(f'A lista possui {len(num)} elementos')