#Um programa que recebeuma frase e informa se é ou não um palíndromo.

phrase = str(input('Digite a frase ')).upper().strip()

words = phrase.split()
join = ''.join(words)

inverse = join[::-1] #Frase invertida

if join == inverse:
    print('''O inverso de {} é {}
Portanto é um palíndromo'''.format(join,inverse))
else:
    print('''O inverso de {} é {}
Portanto não é um palíndromo'''.format(join,inverse))