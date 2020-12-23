#Refazer o desafio 61 com uma opção para mostrar mais 5 progressões

pt = int(input('Qual o primeiro termo da PA? '))
r = int(input('E qual a razão? '))
x = pt + (10-1) * r
pa = []
pta = pt

while (len(pa)) < 10:
    pa.append(pta)
    pta += r
    
print(pa)

mais = int(input('Deseja ver mais 5 progressões? SIM [1], NÃO [0]'))

if mais == 1:   
    while (len(pa)) < 15:
        pa.append(pta)
        pta += r
    print(pa)