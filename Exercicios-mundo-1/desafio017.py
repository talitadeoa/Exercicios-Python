#Um programa que lê os valores dos catetos e calcula a hipotenusa

from math import hypot

co = float(input('Digite o valor do cateto oposto... '))
ca = float(input('Digite o valor do cateto adjacente... '))

h = hypot(co,ca)

print('O valor da hipotenusa é {:.2f} '.format (h))