#Função que recebe o ano de nascimento como parâmetro e retorna se está elegível para votar

from datetime import date

def vote(year):
    age = date.today().year - year
    if age < 16:
        return str(f"Com {age} anos: Não vota")
    elif age >= 16 and age < 65:
        return str(f"Com {age} anos: Voto obrigatório")
    else:
        return str(f"Com {age} anos: Voto opcional")
    
vote(int(input('Em que ano você nasceu? ')))


