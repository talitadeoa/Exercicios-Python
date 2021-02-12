#Um programa que recebe varios números até receber o flag 999 e soma todos os valores menos o flag

n = s = c = 0

while True:
    n = int(input('Digite um número inteiro (999 para parar)... '))
    if n == 999:
        break 
    s += n
    c += 2
print(f'O valor total dos {c} valores é: {s}')
