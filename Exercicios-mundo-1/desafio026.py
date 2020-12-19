#Um programa que lê uma string e fala quantas vezes a letra "a" se repete
#Em que posição aparece na primeira e ultima vez

frase = str(input('Digite uma frase... ')).strip().lower()

print("""A letra "a" aparece {} vezes
Sendo a primeira vez na posição {}
E a última vez na posição {}""".format(frase.count('a'),frase.find('a')+1,frase.rfind('a')-frase.count(' ')+1))