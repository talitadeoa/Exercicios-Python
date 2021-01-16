#Um programa que mostra atabuada de um inteiro qualquer digitado pelo usuário, o programa é encerrado quando o valor inserido for negativo

n = count = result = 0

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print(f'\n A tabuada de {n} é:')
    while count < 11:
        print(f'{n} x {count} = {result}')
        count += 1
        result = n*count