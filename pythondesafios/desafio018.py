import math

a = float(input('Entre com um ângulo qualquer em graus: '))

ângulo = math.radians(a)

seno = math.sin(ângulo)
cosseno = math.cos(ângulo)
tangente = math.tan(ângulo)

a_rad = math.pi * a / 180

print('O seno vale {:.3f}, o cosseno vale {:.3f} e a tangente vale {:.3f}.'.format(math.sin(a_rad), math.cos(a_rad), math.tan(a_rad)))
print('O seno vale {:.3f}, o cosseno vale {:.3f} e a tangente vale {:.3f}.'.format(seno, cosseno, tangente))
print('O seno vale {:.3f}, o cosseno vale {:.3f} e a tangente vale {:.3f}.'.format(math.sin(math.radians(a)), math.cos(math.radians(a)), math.tan(math.radians(a))))
