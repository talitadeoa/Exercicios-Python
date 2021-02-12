#Um programa que simula um caixa eletrônico
#O usuario informa o valor que deseja sacar e o programa calcula em quantas notas de $50, $20, $10, ou $1 será feito o saque

value = bill50 = bill20 = bill10 = bill1 = 0

while value == 0:
    value = int(input('Qual o valor que deseja sacar? R%'))
    while value/50 >= 1:
        bill50 = value//50
        value = value - bill50*50

