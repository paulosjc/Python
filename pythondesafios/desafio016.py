import math

num = float(input('Digite um número: '))
print('A parte inteira de {} é {}'.format(num, math.floor(num)))
print('A parte inteira de {} é {}'.format(num, math.trunc(num)))
print('A parte inteira de {} é {}'.format(num, int(num)))
print('A parte inteira de {} é {:.0f}'.format(num, num // 1))
