#Um programa que usa a matriz do desafio anterior para analisar seus dados e encontrar as seguintes respostas:
#a)Soma de valores pares
#b)Soma de valores da terceira coluna
#c)Maior valor da segunda linha

temp = []
array = []
arrayx = [[],[],[]]
arrayy = [[],[],[]]
even = []
#y3 = []
x = y = maxy3 = 0

for i in range (0,9):
    if i <= 2:
        x = 0
    if i > 2 and i <= 5:
        x = 1
    if i > 5 and i <= 8:
        x = 2
    temp.append(int(input(f'Digite o número para a posição [{x},{y}] ')))
    array.append(temp[:])         
    arrayx[x].append(temp[:])    
    y += 1  
    if y >= 3:
        y = 0   
    arrayy[y].append(temp[:])    
    temp.clear()   

    if array[i][0] %2 == 0:
        even.append(array[i][0])    



for i in range (len(arrayx)):
    print(arrayx[i])

#sum(even)    

