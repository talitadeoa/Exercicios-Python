#Um programa que usa a matriz do desafio anterior para analisar seus dados e encontrar as seguintes respostas:
#a)Soma de valores pares
#b)Soma de valores da terceira coluna
#c)Maior valor da segunda linha

temp = []
array = []
arrayx = [[],[],[]]
arrayy = [[],[],[]]
even = []
x = y = 0

for i in range (0,9):
    if i <= 2:
        x = 0
    if i > 2 and i <= 5:
        x = 1
    if i > 5 and i <= 8:
        x = 2
    temp.append(int(input(f'Digite o número para a posição [{x},{y}] ')))
    array.append(temp[:])       
    arrayx[x].append(temp[0])    
    arrayy[y].append(temp[0]) 
    temp.clear()       
    y += 1  
    if y >= 3:
        y = 0   

    if array[i][0] %2 == 0:
        even.append(array[i][0])    

for i in range (len(array)):
    print(f'{array[i]}')

print(f'''
A soma de todos os valores pares é {sum(even)}
A soma dos valores da terceira coluna é {sum(arrayy[2])}
O maior valor da segunda linha é {max(arrayx[1])}''')
