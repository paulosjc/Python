peso = float(input('Digite o seu peso em kg: '))
altura = float(input('Qual é a sua altura em metros? '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Você está abaixo do peso! Coma mais...')
elif imc >= 18.5 and imc < 25:
    print('Você está com o peso ideal. \033[34mParabéns!')
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso! \033[33mFaça uma dieta!')
elif imc >= 30 and imc < 40:
    print('Você está obeso...\033[31mComece um regime e faça exercícios!')
else:
    print('Você está com obesidade mórbida! \033[35mVocê deve começar um tratamento urgente!')