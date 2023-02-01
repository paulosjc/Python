nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {}!'.format(nome))
print('É um prazer te conhecer {:20}!'.format(nome))
print('Muito prazer em te conhecer {:>20}!'.format(nome))
print('É um prazer te conhecer {:<20}!'.format(nome))
print('Que prazer te conhecer {:^20}!'.format(nome))
print('Que prazer te conhecer {:=^20}!'.format(nome))
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}, o produto é {} e a divisão é {:.3f}.'.format(s, m, d), end = ' >>> ')
print('A divisão inteira é {} e a exponenciação é {}.'.format(di, e))
print('A soma vale {}, \no produto é {} \ne a divisão é {:.3f}.'.format(s, m, d))
