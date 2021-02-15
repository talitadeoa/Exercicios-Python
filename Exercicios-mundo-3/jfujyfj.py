products = ('leite', 3.00, 'arroz', 127.00, 'chocolate', 6.00, 'feijao', 9.00)

for i in products:
    if type(i) is str:
        print(f'{i:.<30}', end='')
    else:
        print(f'R$ {i:>7.2f}')
print('--'*20)