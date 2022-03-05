#Uma função semelhante a input que recebe e valida apenas números inteiros

def leiaInt(msg):
    inter = input(msg)
    while not inter.isdigit():
        print('Por favor digite apenas um inteiro válido')    
        inter = input(msg)
    return inter

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar {n}')