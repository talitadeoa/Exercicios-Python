#Um programa que lê 5 valores, armazena em uma lista e ao final mostra o maior e menor e suas respectivas posições na lista

numbers = []

for n in range(0,5):
    num = int(input(f'Digite o {n+1}º número: '))
    numbers.append(num)

    if n == 0:
        b = num
        pb = n
        s = num
        ps = n
    if num > b:
        pb = n
        b = num
    if num < s:
        ps = n
        s = num

print(f'''\nOs valores inseridos foram: {numbers}
O maior valor é {b} na posição {pb}
O menor {s} na posição {ps} ''')