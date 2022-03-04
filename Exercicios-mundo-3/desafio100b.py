#Um programa com duas fonções, uma sorteia números e outra soma os valores pares sorteados e os aloca em listas

from random import randint

sorteados = []
pares = []

def sorteia(i):
    for i in range(i):
        sorteados.append(randint(0,9))

def somapar(sorteados):
    soma = 0
    for i in sorteados:
        if i % 2 == 0:
            pares.append(i)
            soma += i
    print(soma)
    
sorteia(5)
somapar(sorteados)

print(sorteados)
print(pares)
