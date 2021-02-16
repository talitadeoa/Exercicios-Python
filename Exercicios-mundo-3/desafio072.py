#Um programa que lê um número inteiro de 0 a 20 e mostra por extenso

nums = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'


while True:    
    num = int(input('Qual número entre 0 e 20? '))
    while num < 0 or num >20:
        num = int(input('Tente novamente. Qual número entre 0 e 20? '))
    print(nums[num])
    stop = ''
    while stop not in ['S','N']:
        stop = (input('Deseja continuar? [S/N] ')).upper()[0]
    if stop == 'N':
        break

