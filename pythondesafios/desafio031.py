d = float(input('Qual é a distância a ser percorrida na viagem? '))
print('A distância a ser percorrida é de {:.2f} km'.format(d))
if d <= 200:
    print('O custo dessa viagem será de R$ {:.2f}'.format(d * 0.50))
else:
    print('O custo da viagem será de R$ {:.2f}'.format(d * 0.45))
