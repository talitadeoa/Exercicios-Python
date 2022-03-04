#Uma função que recebe um texto e o transofmra em um título adaptável

def escrever(txt):
    bar = int(len(txt)+4)
    print(f'~'* bar)
    print(f'{txt:^{bar}}')
    print(f'~'* bar)
    
escrever(str(input('Digite um título: ')))