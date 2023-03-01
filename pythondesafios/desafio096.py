print(f'{"Controle de terrenos":^30}')
print('-' * 30)

def área(c, l):
    print(f'A área de um terreno de {c:.2f} m x {l:.2f} m é de {c * l:.2f} m².')

área(float(input('Comprimento [m]: ')), float(input('Largura [m]: ')))
