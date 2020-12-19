#Um programa que lê um nome e identifica se há o sobrenome "Silva"

nome = str(input('Qual o seu nome? ')).lower()

tem_silva = nome.find('silva')

print(tem_silva != -1)