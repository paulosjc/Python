d = float(input('Qual é a distância a ser percorrida na viagem? '))
print('Você está prestes a começar uma viagem de {:.2f} km'.format(d))
if d <= 200:
    preço = d * 0.5
else:
    preço = d * 0.45
print('O custo dessa viagem será de R$ {:.2f}'.format(preço))
