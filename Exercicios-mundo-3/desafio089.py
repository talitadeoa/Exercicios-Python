#Um programa que recebe os valores nome do aluno e duas notas, calcula a média, mostra o boletim e também permite verificar as notas de cada aluno individualmente

name = ''
grade_1 = grade_2 = index = 0
report = []
temp = []
temp_grades = []

while True:
    index += 1 
    name = input(f'Qual o nome do {index}º aluno? ')
    grade_1 = int(input('Qual a 1ª nota '))
    grade_2 = int(input('Qual a 2ª nota '))
    temp.append(name)
    temp_grades.append(grade_1)
    temp_grades.append(grade_2)
    temp.append(temp_grades[:])
    report.append(temp[:])
    temp.clear()
    temp_grades.clear()
    state = input('Deseja continuar inserindo notas [S/N]? ').lower()
    while state not in 'sn':
        state = input('Deseja continuar inserindo notas [S/N]? ').lower()
    if state == 'n':
        break

print(report)