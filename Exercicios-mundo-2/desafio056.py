#Um programa que lê o nome, idade e sexo de 4 pessoas e retorna a média de idade do grupo, o nome do homem mais velho e quantas mulheres tem menos de 20 anos.

nomes = []
idades = []
sexos = []
media = 0

for pessoa in range (1,5):
    #nomes.append(input(f'Qual o nome da {pessoa}ª pessoa? '))
    idades.append(int(input(f'Qual a idade da {pessoa}ª pessoa? ')))
    #sexos.append(input(f'Qual o sexo da {pessoa}ª pessoa? M para mulher e H para homem ')).upper()
    media += idades[pessoa]/4
    if sexo:


print(idades,media)

