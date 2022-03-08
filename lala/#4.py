
def piramide(altura):
    i = altura-1
    largura = 1
    while i > 0:
        print(' '*(i), end='')
        i -= 1
        if largura < altura:
            print('#'*(largura))
            largura += 1

n = int(input('Qual a altura? '))
piramide(n)
        
        