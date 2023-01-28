import math

co = float(input('Entre com a medida do cateto oposto: '))
ca = float(input('Entre com a medida do cateto adjacente: '))
h1 = math.sqrt(math.pow(co, 2) + math.pow(ca, 2))
h2 = (ca ** 2 + co ** 2) ** (1/2)
h3 = math.hypot(co, ca)
print('A hipotenusa vale {}'.format(h1))
print('A hipotenusa é: {}'.format(h2))
print('A hipotenusa tem o valor de: {}'.format(h3))
