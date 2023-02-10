num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')))
print(f'Você digitou os valores {num}')
print(f'Você digitou {num.count(9)} vezes o número 9')

if 3 in num:
       print(f'O valor 3 apareceu pela primeira vez na {num.index(3) + 1}ª posição')
else:
       print('O valor 3 não foi digitado')
print('Os valores pares são: ', end='')
for c in num:
       if c % 2 == 0:
              print(c, end=' ')

