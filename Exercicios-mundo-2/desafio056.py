#Um programa que lê o nome, idade e sexo de 4 pessoas e retorna a média de idade do grupo, o nome do homem mais velho e quantas mulheres tem menos de 20 anos.

nomes = []
idades = []
sexos = []
media = 0
mvn = ''
mvi = 0
m20 = 0

for pessoa in range (1,5):
    print(f'----- {pessoa}ªPESSOA -----')
    nome = (input(f'NOME: '))
    nomes.append(nome)
    idade = (int(input(f'IDADE: ')))
    idades.append(idade)
    sexo = (input(f'SEXO: [M/F] ')).upper()
    sexos.append(sexo)

    media += idades[pessoa-1]/4

    if sexo == 'M' and idade > mvi:
        mvi = idade
        mvn = nome

    if sexo == 'F' and idade < 20:
        m20 += 1

print(f'''A médias das idades {idades} é: {media}
{mvn} é o homem mais velho e tem: {mvi} anos
E {m20} mulheres tem menos de 20 anos''')

