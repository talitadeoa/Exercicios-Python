#Um programa que lê 7 valores, armazena em uma lista composta, separada por pares e ímpares, ao final mostra números pares e ímpares separadamente em ordem crescente

values = [[],[]]
temp = []

for i in range(0,4):
    temp.append(int(input('Digite um valor_')))
    if temp[i]%2==0:
        values[0].append(temp[i])
    else:
        values[1].append(temp[i])      
values[0].sort()
values[1].sort()
print(values)
