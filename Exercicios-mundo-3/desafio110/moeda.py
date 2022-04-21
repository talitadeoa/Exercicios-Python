
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

def resumo(p,a,d):
    tit('Resumo de Valores')
    print(f'O preço analisado é: {p}')
    print(f'A metade é: {metade(p,True)}')
    print(f'O dobro é: {dobro(p,True)}')
    print(f'{a}% de Aumento: {aumentar(p,a,True)}')
    print(f'{d}% de Desconto: {diminuir(p,d,True)}')    
    linha()
