#Programa que cria uma matriz 3x3 com números inseridos pelo usuário

array = [[[],[],[]],[[],[],[]],[[],[],[]]]

for i in range (0,9):
    value = int(input(f'Digite o número para a posição [,]'))
    if i <= 2:
        array[0].append(value)
    if i > 2 and i <= 5:
        array[1].append(value)        
    if i > 5:
        array[2].append(value)  

print(f'{array[0]} \n{array[1]} \n{array[2]}')