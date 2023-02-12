num = []

while True:
    num.append(int(input('Digite um número: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(num)
print(sorted(num))
l = []
for i in num:
    if i not in l:
        l.append(i)
print(sorted(l))

