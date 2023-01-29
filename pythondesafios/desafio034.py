sal = float(input('Qual é o salário do funcionário? '))

if sal <= 1250:
    print('O aumento é de 15%, passando a ser de R$ {:.2f}'.format(sal * 1.15))
else:
    print('O aumento é de 10%, passando a ser de R$ {:.2f}'.format(sal * 1.10))