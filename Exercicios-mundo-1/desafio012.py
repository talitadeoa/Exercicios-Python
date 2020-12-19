#Um algoritimo que recebe o valor de um produto e calcula com um descont de 5%

preço = float(input('Qual o valor do produto? '))

novo_preço = preço - (preço*5/100)

#p = preço/100
#desconto = float(5*p)
#novo_preço = preço-desconto

print('O valor do produto com desonto é {:.2f}'.format(novo_preço))