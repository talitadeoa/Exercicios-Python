
def aumentar(n,p,formatar=False):
    v = n + (n * p / 100)
    if formatar:
        return moeda(v)
    else:
        return v
      
def diminuir(n,p,formatar=False):
    v = n - (n * p / 100)
    if formatar:
        return moeda(v)
    else:
        return v
        
def dobro(n,formatar=False):
    v = n*2
    if formatar:
        return moeda(v)
    else:
        return v 
    
def metade(n,formatar=False):
    v = n/2
    if formatar:
        return moeda(v)
    else:
        return v
    
def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:>2.2f}'.replace('.', ',')