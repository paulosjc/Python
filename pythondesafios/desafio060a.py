num = int(input('Digite um número cujo fatorial deve ser calculado: '))
fat = 1
n = num
while n > 0:
    fat = fat * n
    n -= 1
print('O fatorial de {} vale {}'.format(num, fat))

