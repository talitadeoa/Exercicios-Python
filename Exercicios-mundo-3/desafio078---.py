#Um programa que lê 5 valores, armazena em uma lista e ao final mostra o maior e menor e suas respectivas posições na lista

numbers = []
pb = ps = 0

for n in range(0,5):
    num = int(input(f'Digite o {n+1}º número: '))
    numbers.append(num)

    if n == 0:
        b = num
        pb.append(n)
        s = num
        ps.append(n)
    if num >= b:        
        b = num
        pb.append(n)

    if num <= s:
        s = num
        ps.append(n)

print(f'''\nOs valores inseridos foram: {numbers}
O maior valor é {b} na posição {pb}
O menor {s} na posição {ps} ''')