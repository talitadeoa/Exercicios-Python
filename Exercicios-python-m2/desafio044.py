#Um gerenciador de pagementos simples

preco = float(input('Qual o valor da compra? '))
pagamento = int(input("""Qual será a forma de pagamento? 
Digite 0 para pagamento à vista no dinheiro ou cheque
Digite 1 para pagamento à vista no cartão
Digite 2 para pagamento parcelado em até 2x
Digite 3 para pagamento parcelado em 3x ou mais 
"""))

if pagamento == 0:
    pagamento = 'pagamento à vista em dinheiro ou cheque'
    saldo = preco - (preco*10/100)
    print("""Você escolheu a opção {}
    Você irá pagar {}""".format(pagamento,saldo))
elif pagamento == 1:
    pagamento = 'pagamento à vista no cartão'
    saldo = preco - (preco*5/100)
    print("""Você escolheu a opção {}
    Você irá pagar {}""".format(pagamento,saldo))
elif pagamento == 2:
    pagamento = 'pagamento parcelado em até 2x'
    saldo = preco
    print("""Você escolheu a opção {}
    Você irá pagar {}""".format(pagamento,saldo))
elif pagamento == 3:
    pagamento = 'pagamento parcelado em 3x ou mais'
    saldo = preco + (preco*20/100)
    print("""Você escolheu a opção {}
    Você irá pagar {}""".format(pagamento,saldo))