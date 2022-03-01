#Função para calcular área

def area(b,h):
    A = b * h
    print(f'''\nLargura: {b}m
Comprimento: {h}m
A área de um terreno {b}x{h} é {A}m²''')

area(float(input('Qual a largura do terreno em metros? ')),float(input('Qual o comprimento do terreno em metros? ')))