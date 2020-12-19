#Um programa que lê 3 número e fala qual o maior e qual o menor

n1= float(input("Digite um número... "))
n2= float(input("Digite mais um número... "))
n3= float(input('Digite outro... '))

maior = n1
menor = n1

if n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3

if n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n2 and n3 < n1:
    menor = n3

print("""O maior número é {:.0f}
E o menor número é {:.0f}""".format(maior,menor))