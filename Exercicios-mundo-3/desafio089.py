#Um programa que recebe os valores nome do aluno e duas notas, calcula a média, mostra o boletim e também permite verificar as notas de cada aluno individualmente

report = []
index = 0
ind = ''

while True:
    index += 1
    name = input(f'Qual o nome do {index}º aluno? ')
    grade_1 = float(input('1ª Nota: '))
    grade_2 = float(input('2ª Nota: '))
    average = (grade_1+grade_2)/2
    report.append([name, [grade_1,grade_2], average])
    state = input('Deseja continuar inserindo notas [S/N]? ').lower()
    while state not in 'sn':
        state = input('Deseja continuar inserindo notas [S/N]? ').lower()
    if state == 'n':
        break

print('-='*30)
print(f'{"No.":<4}{"Aluno(a)":<10}{"Média":<8}')
print('-'*26)
for i, s in enumerate(report):
    print(f'{i:<4}{s[0]:<10}{s[2]:<8.1f}')

while True:
    ind = int(input('\nDeseja visualizar as notas de um aluno específico? Se sim digite seu número [999 para interromper] '))
    if ind == 999:
        print('\ntiau')
        break
    if ind < len(report):
         print(f'As notas de {report[ind][0]} foram: {report[ind][1]}')
