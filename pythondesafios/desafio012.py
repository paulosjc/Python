p = float(input('Qual é o preço do produto? '))
np = p * 0.95
print(f'O novo preço do produto com 5% de desconto é de {np:.2f}')
print('Este produto que custa {:.2f} com 5% de desconto passa a custar {:.2f}'.format(p, np))
