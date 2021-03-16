#Um programa que lê 7 valores, armazena em uma lista composta, separada por pares e ímpares, ao final mostra números pares e ímpares separadamente em ordem crescente

values = [[],[]]
temp = []

for i in range(0,7):
    temp.append(int(input('Digite um valor_')))
    if temp[i]%2==0:
        values.insert(values[0][0], temp[i])
    else:
        values.insert(values[1],[0], temp[i])      

print(values)
