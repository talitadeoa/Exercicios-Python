#Refaça o desafio 051 usando o while

pt = int(input('Qual o primeiro termo da PA? '))
r = int(input('E qual a razão? '))
x = pt + (10-1) * r
pa = []
pta = pt

while (len(pa)) < 10:
    pa.append(pta)
    pta += r
    
print(pa)