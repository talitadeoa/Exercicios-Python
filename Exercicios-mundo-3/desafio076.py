#Um programa que apartir de uma tupla de produtos e preços gera uma tabela

products = ('leite', 3.00, 'arroz', 7.00, 'chocolate', 6.00, 'feijao', 9.00)

print('-'*40)
print('{: ^40}'.format(' Listagem de produtos '))
print('-'*40)

for p in products,1:
    print('{: ^40}'.format(p))
