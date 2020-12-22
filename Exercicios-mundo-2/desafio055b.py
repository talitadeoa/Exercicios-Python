#Um programa que lê o peso de 5 pessoas e informa qual o maior e menor peso

pesos = []
peso = 0

for pessoa in range(1,6):
    peso = (float(input(f'Qual o peso da {pessoa}ª pessoa? ')))   
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O menor peso é: {menor}Kg\nO maior peso é {maior}Kg')    

