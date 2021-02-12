#Um programa que cria uma lista de compras com nome e preço e ao final informa o total gasto nas compras, quantos produtos custam mais de R$1000 e qual o produto mais barato

product = ''
price = 0
shopping = []
prices = []
mt1000 = []
cheapest = 0
stop = False

while stop is not False: 
    product = input('Qual o produto? ')
    while price < 0:
        price = input('Qual o valor do produto? R$')