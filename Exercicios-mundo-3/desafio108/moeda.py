
def aumentar(n,p):
    return n + (n * p / 100)
    
def diminuir(n,p):
    return n - (n * p / 100)
    
def dobro(n):
    return n*2
    
def metade(n):
    return n/2

def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:>2.2f}'.replace('.', ',')