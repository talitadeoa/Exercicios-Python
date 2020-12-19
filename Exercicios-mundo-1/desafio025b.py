#Um programa que lê um nome e identifica se há o sobrenome "Silva"

nome = str(input('Qual o seu nome? ')).strip()

print('Seu nome tem silva: {}'.format('silva' in nome.lower()))