#Um programa que recebe 3 valores e calcula se esses segmentos podem se tornar um triangulo
print('-='*11)
print('Analisador de triângulo... ')
print('-='*11)

s1= float(input('Digite o primeiro valor... '))
s2= float(input('Digite o segundo valor... '))
s3= float(input('Digite o terceiro valor... '))

if s1+s2 > s3 and s1+s3 > s2 and s2+s3 > s1:
    print('Sim, esses valores podem formar um triângulo!')
    if s1 != s2 and s1 != s3 and s2 != s3:
        print('Esses valores formam um triângulo Escaleno')
    elif s1 == s2 and s1 == s3 and s2 == s3:
        print('Esses valores formam um triângulo Équilatero')
    else:
        print('Esses valores formariam um triângulo Isósceles')
else:
    print('Não, esses valores não podem formar um triângulo. Tente novamente! ')

