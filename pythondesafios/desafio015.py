tempo = int(input('Por quantos dias ele ficou alugado? '))
dist = float(input('Ele percorreu quantos km durante esse período? '))
preço = 60 * tempo + 0.15 * dist
print('Você deve pagar R$ {:.2f} pelo aluguel do carro por {} dias.'.format(preço, tempo))
