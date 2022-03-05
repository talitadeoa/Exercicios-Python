#Uma função que calcula um um fatorial, recebe dois parâmetros o número a ser calculado e um boleano para mostraro calculo ou não

def fatorial(num=1, show=False):
    f = 1 
    print(f'''Fatorial de {num}:''')
    print(f'{num}! -> ', end ='')
    for i in range(num, 0, -1):
        f *= i
        if show == True:
            return str(f'{i} -> ')
        else: 
            return f


print(fatorial(5,True))
        