#Um programa que usa a matriz do desafio anterior para analisar seus dados e encontrar as seguintes respostas:
#a)Soma de valores pares
#b)Soma de valores da terceira coluna
#c)Maior valor da segunda linha

array = [[[],[],[]],[[],[],[]],[[],[],[]]]
temp = []
x = y = sum_evens = sum_y2 = max_x1 = 0
 
for x in range (0,3):
    for y in range(0,3):
        array[x][y] = int(input(f'Digite o número para a posição [{x},{y}] '))
for x in range (0,3):
    for y in range(0,3):
        print(f'[{array[x][y]:^5}]', end='')   
        if array[x][y] % 2 == 0:
            sum_evens += array[x][y]
    print()
for y in (0,3):
    sum_y2 += array[y][2]
for in

print(f'''
A soma de todos os valores pares é {sum_evens}
A soma dos valores da terceira coluna é {sum_y2}
O maior valor da segunda linha é {max_x1}''')