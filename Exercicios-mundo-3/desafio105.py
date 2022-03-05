#Uma função capaz de receber varias notas, retorna um dicionário com os dados: quantidade de notas inseridas, maior e menor nota, média e a situação (opcional)

def notas(*n,sit=False):
    """
    -> Analisa as notas e situação de vários alunos
    :param n: Recebe os valores das notas
    :param sit: Opciona, indicando se deve ou não mostra a situação
    :return: Retorna um dicionário com todas as informações
    """
    dict = {'total':len(n),'maior':max(n),'menor':min(n),'media':sum(n)/(len(n))}
    if sit:
        if dict['media'] > 7:
            dict['situação'] = "Boa"   
            return dict  
        elif 7 > dict['media'] > 6:
            dict['situação'] = "Razoável"
            return dict     
        else:
            dict['situação'] = "Ruim"  
            return dict   
    else:
        return dict  

print(notas(3,5,0.2,sit=True))   
print(notas(3,5,0.2))    
print(notas(9,8,8.2,sit=True))   
print(notas(6,5,7.2))   