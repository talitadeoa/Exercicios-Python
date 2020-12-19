#Um programa que calcula o valor de uma viagem

kms = float(input("Quantos Kms até o seu destino? "))

if kms >= 200:
    preço = kms*0.45
else:
    preço = kms*0.50

print("O custo da sua viagem será R${:.2f}".format(preço))