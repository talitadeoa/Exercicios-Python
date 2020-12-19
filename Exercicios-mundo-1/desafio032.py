#Um programa que calcula se um ano é bissexto
from datetime import date

ano = int(input("Digite um ano... "))

if ano == 0:
    ano = date.today().year

bissexto1 = ano % 4
bissexto2 = ano % 100
bissexto3 = ano % 400

if bissexto1 == 0:
    if bissexto2 != 0 or bissexto3 == 0:
        print("é bissexto")
    else:
        print("n é bissexto2")            
else:
    print("n é bissexto1")
