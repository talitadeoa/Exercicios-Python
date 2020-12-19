#Um programa que calcula o preço a pagar por um carro alugado apartir dos dias usados e kilometros rodado

dias = int(input('Quantos dias foi alugado? '))
kms = float(input('Quantos kilometros foram rodados? '))

valor = (dias*60)+kms*0.15

print('O total a pagar é de R${:.2f}' .format(valor))