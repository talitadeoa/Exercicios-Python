#Um programa que apartir de uma tupla de produtos e preços gera uma tabela

products = ('leite', 3.00, 'arroz', 127.00, 'chocolate', 6.00, 'feijao', 9.00)

print('--'*20)
print(f'Listagem de produtos{:^40}')
print('--'*20)

for i in products:
    if type(i) is str:
        print(f'{i:.<30}', end='')
    else:
        print(f'R$ {i:>7.2f}')
print('--'*20)