#Um programa que simula um caixa eletrônico
#O usuario informa o valor que deseja sacar e o programa calcula em quantas notas de $50, $20, $10, ou $1 será feito o saque

value = bill50 = bill20 = bill10 = bill1 = 0
ok = False

while ok is not True:
    value = int(input('Qual o valor que deseja sacar? R%'))
    while value <=0:
        value = int(input('Qual o valor que deseja sacar? R%'))
    while value/50 >= 1:
        bill50 = value//50
        value = value - bill50*50
    while value/20 >= 1:
        bill20 = value//20
        value = value - bill20*20
    while value/10 >= 1:
        bill10 = value//10
        value = value - bill10*10
    while value/1 >= 1:
        bill1 = value
        value = 0
    ok = True

print(f'{bill50} Notas de R$50 \n{bill20} Notas de R$20 \n{bill10} Notas de R$10 \n{bill1} Notas de R$1')

