#Programa que cria uma matriz 3x3 com números inseridos pelo usuário

array = [[[],[],[]],[[],[],[]],[[],[],[]]]
temp = []
x = y = 0

for x in range (0,3):
    for y in range(0,3):
        array[x][y] = int(input(f'Digite o número para a posição [{x},{y}] '))
for x in range (0,3):
    for y in range(0,3):
        print(f'[{array[x][y]:^5}]', end='')
    print()

