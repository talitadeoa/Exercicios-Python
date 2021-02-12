#Um programa que simula um caixa eletrônico
#O usuario informa o valor que deseja sacar e o programa calcula em quantas notas de $50, $20, $10, ou $1 será feito o saque

value = bill50 = bill20 = bill10 = bill1 = 0

while value == 0:
    value = int(input('Qual o valor que deseja sacar? R%'))
    while value/50 > 0:
        bill50 = value//50
        value = value - bill50*50
    while value/20 > 0:
        bill20 = value//20
        value = value - bill20*20
    while value/10 > 0:
        bill10 = value//10
        value = value - bill10*10
    while value/1 > 0:


