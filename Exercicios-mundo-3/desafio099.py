#Função que recebe varios parâmetros e mostra qual o maior valor entre eles

def maior(*num):
    if len(num) > 0:
        maior = num[0]
        print(f'Analisando os valores: ', end='') 
        for i in num:
            print(f'{i}, ', end='')
            if i >= maior:
                maior = i
        print(f'foram inseridos {len(num)} valores sendo o maior deles {maior}.')
    else:
        print('Nenhum valor inserido')

maior(3,2,4,5,6)    
maior(1)
maior()
maior(2,7,1,3000,0,22)