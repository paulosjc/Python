import math
import random

num = float(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz quadrada de {} é igual a {:.2f}'.format(num, raiz))
print('A raiz quadrada de {} vale {}'.format(num, math.floor(raiz)))
print('A raiz quadrada de {} vale {}.'.format(num, math.ceil(raiz)))
print('A raiz quadrada de {} é {:.2f}.'.format(num, round(raiz)))

n = random.random()
print('{:.2f}'.format(n))
print(f'{n:.2f}')

p = random.randint(1, 10)
print(p)
