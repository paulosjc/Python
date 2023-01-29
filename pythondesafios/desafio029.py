v = float(input('Qual foi a velocidade medida? '))
print('A velocidade medida foi de {:.2f} km/h'.format(v))

if v >= 80:
    print('Você ultrapassou o limite de velocidade da via!')
    print('Você será multado em R$ {:.2f}'.format((v - 80) * 7))
