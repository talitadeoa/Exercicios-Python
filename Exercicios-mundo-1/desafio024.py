#Um programa que lê o nome de uma cidade e diz se ela começa ou não com a palavra "santo"

cidade = input('Digite o nome da cidade... ').strip()

print(cidade[:5].lower()=='santo')
