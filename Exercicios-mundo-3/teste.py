temp = []
array = []
evens = []
x = y = 0
array_x = [[],[],[]]
array_y = [[],[],[]]
total = (len(array_x)*len(array_y))

for i in range (0,total):
    if i % len(array_x) == 0 and i != 0:
        x += 1
    temp.append(int(input(f'Digite o número para a posição [{x},{y}] ')))
    array.append(temp[:])       
    array_x[x].append(temp[0])    
    array_y[y].append(temp[0]) 
    temp.clear()         
    y += 1  
    if y >= len(array_y):
        y = 0   

    if array[i][0] %2 == 0:
        evens.append(array[i][0])    

for i in range (len(array_x)):
    print(f'\n{array_x[i]}')

print(f'''
A soma de todos os valores pares é {sum(evens)}
A soma dos valores da terceira coluna é {sum(array_y[2])}
O maior valor da segunda linha é {max(array_x[1])}''')