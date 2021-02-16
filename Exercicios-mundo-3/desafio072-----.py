#Um programa que lê um número inteiro de 0 a 20 e mostra por extenso

nums = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
stop = False

while stop is not True:
    num = int(input('Qual número entre 0 e 20? '))
    if 0 <= num <= 20:
        break
    else:
        print('Tente novamente. ', end ='')
    stop
print(nums[num])