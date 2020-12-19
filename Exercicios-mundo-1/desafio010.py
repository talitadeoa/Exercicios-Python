#Um programa que armazena o valorem R$ e converte para US$ (Usando a cotação de R$5,74 (01/11/20))

carteira = float(input('Quanto dinheiro você tem em sua carteira? R$'))

dolar = float(5.74)

quantos_dolares = carteira/dolar

print('Com R${:.2f} Você pode comprar U${:.2f} doláres' .format(carteira,quantos_dolares))