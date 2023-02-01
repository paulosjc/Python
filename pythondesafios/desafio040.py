n1 = float(input('Entre com a primeira nota: '))
n2 = float(input('Entre com a segunda nota: '))

m = (n1 + n2) / 2

if m < 5:
    print('Sua média é de {:.2f}. Você foi \033[31mreprovado\033[m! Estude mais!'.format(m))
elif m >= 5 and m < 7:
    print('Sua média de {:.2f} não é suficiente para ser \033[33maprovado\033[m. Você está de recuperação!'.format(m))
else:
    print('Sua média é de {:.2f}, portanto você está \033[34maprovado\033[m! Parabéns!'.format(m))
