#Um programa que apartir de uma tupla de produtos e preços gera uma tabela

products = ('leite', 3.00, 'arroz', 127.00, 'chocolate', 6.00, 'feijao', 9.00)

print('-'*40)
print(f'{"Listagem de produtos": ^40}')
print('-'*40)

for p in range (0,len(products),2):
    print(f"{products[p]:.<30}", f"R${products[p+1]:>7.2f}")

print('--'*20)