num = int(input('Digite um número cujo fatorial deve ser calculado: '))
fat = 1
n = num
for n in range(num, 0, -1) :
    fat = fat * n
print('O fatorial de {} vale {}'.format(num, fat))