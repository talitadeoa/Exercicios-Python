#Um programa que lê um número inteiro de 0 a 20 e mostra por extenso

nums = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'

num = int(input('Qual número entre 0 e 20? '))

while num < 0 or num > 20:
    num = int(input('Qual número entre 0 e 20? '))

print(nums[num])