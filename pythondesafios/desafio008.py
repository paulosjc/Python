m = float(input('Digite a medida em metros: '))
#print('A medida digitada em metros corresponde a {} cm e {} mm.'.format(m * 100, m * 1000))
print('A medida digitada em metros corresponde a: \n{} km \n{} hm \n{} dam \n{} dm \n{} cm \n{} mm.'.format(m / 1000, m / 100, m / 10, m * 10, m * 100, m * 1000))
