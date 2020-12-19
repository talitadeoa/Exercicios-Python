#Um programa que armazena o valor em US$ e converte para R$ (Usando a cotação de R$5,74 (01/11/20))

carteira = float(input('Quanto dolares você tem? '))

dolar = float(5.74)

quantos_reais = carteira*dolar

print('Você tem {:.2f} reais' .format(quantos_reais))