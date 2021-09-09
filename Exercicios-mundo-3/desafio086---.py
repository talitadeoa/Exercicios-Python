#Programa que cria uma matriz 3x3 com números inseridos pelo usuário

array = []
temp = []
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
    temp.clear()
    y += 1  
    if y >= 3:
        y = 0    
        
print(f"""
{array[0]} {array[1]} {array[2]}
{array[3]} {array[4]} {array[5]}
{array[6]} {array[7]} {array[8]}""")