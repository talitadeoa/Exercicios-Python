#Um programa que lê o nome completo e escreve o primeiro e último nome

nome = str(input('Qual o seu nome? '))

nomel = nome.split()

print("""Seu pimeiro nome é {}
Seu último nome é {}""".format(nomel[0],nomel[len(nomel)-1]))

print(nomel)
print(len(nomel))
