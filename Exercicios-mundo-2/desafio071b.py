#Um programa que simula um caixa eletrônico
#O usuario informa o value que deseja sacar e o programa calcula em quantas notas de $50, $20, $10, ou $1 será feito o saque

value =  int(input('Qual o valor que você deseja sacar? R$')
(total) = value
(bill) = 50
(totalbill) = 0

while True
    if total >= bill:
        total -= bill
        totalbill += 1
    else:
        print(f'{totalbill} notas de R${bill:.2f}')
        if bill == 50:
            bill = 20    
        elif bill == 20:
            bill = 10
        elif bill == 10:
            bill = 1
        totalbill = 0
        if total == 0:
            break

    