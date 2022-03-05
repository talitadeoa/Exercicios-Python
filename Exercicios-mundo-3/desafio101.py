#Função que recebe o ano de nascimento como parâmetro e retorna se está elegível para votar

from datetime import date

def vote(year):
    age = date.today().year - year
    if age < 16:
        return str(f"Com {age} anos: Não vota")
    elif 16 <= age < 18 or age > 65:
        return str(f"Com {age} anos: Voto opcional")
    else:
        return str(f"Com {age} anos: Voto obrigatório")
    
print(vote(int(input('Em que ano você nasceu? '))))


