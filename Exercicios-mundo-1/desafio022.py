#Um programa que recebe o input de um nome e reescreve de diferentes formas

nome = input('Digite o nome... ')

p = nome.split()

print("""Nome em letras maisúculas: {};
Nome em letras minísculas {}
Letras ao total: {}
Letras do primeiro nome: {}""".format(nome.upper(),nome.lower(),len(nome)-nome.count(' '),len(p[0])))

nome.find(' ')

print(nome.find(' '))