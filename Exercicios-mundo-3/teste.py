#Um programa com um dicionário que armazena dados do aluno como nome e média e ao fim mostra sua situação se aprovado ou não

aluno = {}

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))

if aluno['media'] < 7:
    aluno['status'] = 'Reprovado'
else:
    aluno['status'] = 'Aprovado'
    
print(f'\nO aluno {aluno["nome"]} com média {aluno["media"]} foi {aluno["status"]}')