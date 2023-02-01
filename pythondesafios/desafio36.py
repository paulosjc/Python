valor = float(input('Qual é o valor da casa? '))
salário = float(input('Qual é o seu salário líquido? '))
anos = int(input('Em quantos anos você pretende pagar este imóvel? '))

meses = anos * 12
parcela = valor / meses

if parcela <= salário * 0.3:
    print('\033[34mPodemos lhe conceder o empréstimo para a compra do imóvel!\033[m')
else:
    print('\033[31mInfelizmente a concessão do empréstimo não será possível...Sentimos muito!\033[m')
