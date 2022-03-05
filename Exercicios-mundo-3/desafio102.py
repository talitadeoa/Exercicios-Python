#Uma função que calcula um um fatorial, recebe dois parâmetros o número a ser calculado e um boleano para mostraro calculo ou não

def fatorial(num=1, show=False):
    """
    ->Calcula o fatorial de um número
    :param a: Valor a ser calculado o fatorial
    :param b: Opção para mostrar ou não o calculo
    :return: O valor do fatorial
    """
    f = 1 
    print(f'''Fatorial de {num}:''')
    print(f'{num}! -> ', end ='')
    for i in range(num, 0, -1):
        if show:
            if i > 1:
                print(f'{i} x ', end='') 
            else:   
                print(f'{i} = ', end='')  
        f *= i
    print(f)
    return f
        
fatorial(5)
fatorial(5,True)
