preço = float(input('Qual é o preço do produto? R$ '))
opção = int(input('Opções:\n1 - pagamento à vista (cheque ou dinheiro)\n2 - compra à vista no cartão\n3 - parcelamento em até 2x no cartão\n4 - parcelamento em 3x ou mais no cartão\nDigite sua escolha: '))
print('O preço do produto é: R$ {:.2f}'.format(preço))
print('Opção escolhida: {}'.format(opção))

if opção == 1:
    print('Opção escolhida: pagamento à vista em cheque ou dinheiro')
    print('O preço a pagar é de R$ {:.2f}'.format(preço * 0.9))
elif opção == 2:
    print('Opção escolhida: compra à vista no cartão')
    print('O preço a pagar é de R$ {:.2f}'.format(preço * 0.95))
elif opção == 3:
    print('Opção escolhida: parcelamento em até 2x no cartão')
    print('O preço a pagar é de R$ {:.2f}'.format(preço))
elif opção == 4:
    print('Opção escolhida: parcelamento em 3x ou mais no cartão')
    print('O preço a pagar é de R$ {:.2f}'.format(preço * 1.2))
else:
    print('Opção inválida')