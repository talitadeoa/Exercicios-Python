
def fatorial(num=1):
    f = 1 
    print(f'''Fatorial de {num}:''')
    print(f'{num}! -> ', end ='')
    for i in range(num, 0, -1):
        print(f'{i} -> ', end='')
        f *= i
    return f


print(fatorial(5))
        