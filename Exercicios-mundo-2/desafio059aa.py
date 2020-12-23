#Um programa que recebe 2 valores e mostra um menu com varias operações possíveis

n1 = float(input('Digite o 1o númeo '))
n2 = float(input('Digite o 2o númeo '))
escolha = 0
soma = float()
multi = float()
maior = float()

while escolha != 5: 
    escolha = int(input('''O que você deseja fazer agora?
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa \n'''))

    if escolha == 1:
        soma = n1+n2
        print(f'A soma dos números {n1} e {n2} é {soma}')
    elif escolha == 2:
        multi = n1*n2
        print(f'A multiplicação dos números {n1} e {n2} é {multi}')   
    elif escolha == 3: 
        if n1 > n2:
            maior = n1    
        if n2 > n1: 
            maior = n2
        print(f'Entre {n1} e {n2} o maior número é {maior}')    
    elif escolha == 4:
        n1 = float(input('Digite o 1o númeo '))
        n2 = float(input('Digite o 2o númeo '))
    elif escolha == 5:
        print('OK, xau')
    else: 
        print('Dados inválidos tente novamente')


