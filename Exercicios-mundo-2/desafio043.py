#Calculadora de IMC

peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura '))
imc = peso/(altura*altura)

if imc <= 18.5:
    print('Seu peso está abaixo do ideal')
elif imc >= 40:
    print('Você tem obesidade morbida')  
elif imc >= 18.5 and imc <25:
    print('Seu peso está ideal para sua altura')
elif imc >= 30 and imc <40:
    print('Você está obeso')
else:
    print('Você está um pouco acima do peso')
