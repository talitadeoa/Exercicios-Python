#Um programa que usa a matriz do desafio anterior para analisar seus dados e encontrar as seguintes respostas:
#a)Soma de valores pares
#b)Soma de valores da terceira coluna
#c)Maior valor da segunda linha

array = []
arrayx = [[],[],[]]
temp = []
y3 = []
even = []
x = y = toteven = maxy3 = 0

for i in range (0,9):
    if i <= 2:
        x = 0
    if i > 2 and i <= 5:
        x = 1
    if i > 5 and i <= 8:
        x = 2
    temp.append(int(input(f'Digite o número para a posição [{x},{y}] ')))
    array.append(temp[:]) 
    if x == 0:
        arrayx[0].append(temp[:])
    elif x == 1:
        arrayx[1].append(temp[:])
    elif x == 2:
        arrayx[2].append(temp[:])
    temp.clear()   
    y += 1  
    if y >= 3:
        y = 0   

    if array[i][0] %2 == 0:
        even.append(array[i][0])
        
toteven = sum(even)    

for i in range (len(arrayx)):
    y3 = sum(arrayx[i][2])

#print(f'''{arrayx[0]}
#{arrayx[1]}
#{arrayx[2]}''')
#print(even,toteven)
print(y3)