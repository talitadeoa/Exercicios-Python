#Um programa que cria uma lista de compras com nome e preço e ao final informa o total gasto nas compras, quantos produtos custam mais de R$1000 e qual o produto mais barato

product = ''
p = cheapest = price = 0
shopping = []
prices = []
mt1000 = []
stop = False

while stop is not True: 
    product = input('Qual o produto? ')
    shopping.append(product)
    price = int(input('Qual o valor do produto? R$'))
    while price == 0:
        price = int(input('Qual o valor do produto? R$'))
    prices.append(price)
    if price >= 1000:
        mt1000.append(p)
    if price < cheapest:
        cheapest = p
    stop = input('Deseja cadastrar mais um produto? [S/N] ').upper()
    while stop not in ['S','N']:
        stop = input('Deseja cadastrar mais um produto? [S/N] ').upper()
    if stop == 'S':
        p+=1
    elif stop == 'N':
        stop = True

print(f'O total das compras foi: R${sum(prices)} \n{len(mt1000)} Produtos custaram mais de R$1000 \nO produto mais barato foi {shopping[cheapest]}')        