#Um programa que analisa se uma expressão é valida

expression = input('Digite a expressão que deseja analisar: ')
countl = 0
countr = 0

for l in expression:
    if '(' == l:
        countl += 1
    elif ')' == l:
        countr += 1
    sumrl = (countl+countr)%2
    elif sumrl!=0 :  
        print('Expressão inválida')
    
    stop = ''
    while stop not in ['S','N']:
        stop = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if stop in 'N':
        break
    
print('Expressão válida!')