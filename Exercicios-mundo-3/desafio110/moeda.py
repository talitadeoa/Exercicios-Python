
cores = ('\033[m',  # sem cores
         '\033[1;97;46m', #cyan
         '\033[1;32;47m', #verde e cinza
         '\033[1;97;45m',  # roxo
         '\033[1;37;43m',  # amarelo
         '\033[7;30;107m'  # branco e preto
         '\033[0;36;47m', #verde e cinza         
         )

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

def linha():
    print('-'*34)

def tit(txt,cor=0):
    bar = int(len(txt)*2)
    print(cores[cor])
    print('='*bar)
    print(f'{txt:^{bar}}')
    print('='*bar)

def resumo(p=0,taxaa=10,taxad=5):
    linha()
    print(f'Resumo de Valores'.center(30))
    linha()
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Metade do preço: \t{metade(p,True)}')
    print(f'Dobro do preço: \t{dobro(p,True)}')
    print(f'{taxaa}% de Aumento: \t{aumentar(p,taxaa,True)}')
    print(f'{taxad}% de Desconto: \t{diminuir(p,taxad,True)}')    
    linha()
