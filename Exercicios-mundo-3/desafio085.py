#Um programa que lê 7 valores, armazena em uma lista composta, separada por pares e ímpares, ao final mostra números pares e ímpares separadamente em ordem crescente

temp = []
values = [[],[]]

for i in range(0,7):
    temp.append(int(input(f'Digite o {i+1}º valor: ')))
    if temp[i]%2==0:
        values[0].append(temp[i])
    else:
        values[1].append(temp[i])      
values[0].sort()
values[1].sort()
print(f'\nOs valores pares são: {values[0]} \nOs valores ímpares são: {values[1]}') 
