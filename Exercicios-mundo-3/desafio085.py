#Um programa que lê 7 valores, armazena em uma lista composta, separada por pares e ímpares, ao final mostra números pares e ímpares separadamente em ordem crescente

values = []
evens_odds = [[],[]]

for i in range(0,7):
    values.append(int(input(f'Digite o {i+1}º valor: ')))
    if values[i]%2==0:
        evens_odds[0].append(values[i])
    else:
        evens_odds[1].append(values[i])    
evens_odds[0].sort()          
evens_odds[1].sort()
print(f'\nOs valores pares são: {evens_odds[0]} \nOs valores ímpares são: {evens_odds[1]}') 
