sal = float(input('Qual é o salário do funcionário? '))
n_sal = sal * 1.15
print('O novo salário do funcionário que ganha R$ {:.2f} é de R$ {:.2f}.'.format(sal, n_sal))
print(f'O salário de R$ {sal:.2f} com 15% de aumento passa a ser de R$ {n_sal:.2f}.')