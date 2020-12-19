#Um programa que lê um angulo qualquer e informa os valores do seno, cosseno e tangente

from math import cos, sin, tan, radians

angulo = float(input('Qual o valor do angulo? '))


cos = cos(radians(angulo))
sen = sin(radians(angulo))
tan = tan(radians(angulo))

print('O valor do cosseno é {:.2f}, do  seno {:.2f} e a tangente {:.2f}'.format((cos),(sen),(tan)))