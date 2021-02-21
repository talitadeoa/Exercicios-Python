#Um programa que analisa se uma expressão é valida

expression = input('Digite a expressão que deseja analisar: ')
stack = []

for char in expression:
    if char == '(':
        stack.append('(')
    elif char == ')': 
        if len(stack)>0:
            stack.pop()
        else:
            stack.append('(')
            break

if len(stack)==0:
    print('Expressão válida')
else:
    print('Expressão inválida')
