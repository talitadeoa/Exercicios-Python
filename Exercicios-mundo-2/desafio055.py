#Um programa que lê o peso de 5 pessoas e informa qual o maior e menor peso

pesos = []
peso = 0

for pessoa in range(1,6):
    pesos.append(float(input(f'Qual o peso da {pessoa}ª pessoa? ')))   
ordem = sorted(pesos)
print(f'O menor peso é: {ordem[0]}Kg\nO maior peso é {ordem[4]}Kg')    

