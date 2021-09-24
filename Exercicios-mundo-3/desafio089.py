#Um programa que recebe os valores nome do aluno e duas notas, calcula a média, mostra o boletim e também permite verificar as notas de cada aluno individualmente

report = []
index = 0

while True:
    index += 1
    name = input(f'Qual o nome do {index}º aluno? ')
    grade_1 = float(input('1ª Nota: '))
    grade_2 = float(input('2ª Nota: '))
    media = (grade_1+grade_2)/2
    report.append([name, [grade_1,grade_2], media])
    state = input('Deseja continuar inserindo notas [S/N]? ').lower()
    while state not in 'sn':
        state = input('Deseja continuar inserindo notas [S/N]? ').lower()
    if state == 'n':
        break
print('-='*30)
print(f'''Boletim de notas:\n
{"No.":<4}{"Aluno(a)":<10}{"Média":<8}\n''')
print('-'*26)
for i, s in enumerate(report):
    print(f'{i:<4}{report[i][0]:<10}{media:<8.1f}')