#Um programa que informas quantas vogais tem cada palavraa de uma tupla

tupla = ('pao', 'feijao', 'macarrao', 'sal', 'suco', 'arroz')

vowel = 0
totalvowel = 0

for i in tupla:
    if 'a','e','i','o','u' in i: 
        vowel += 1
    print(f'A palavra {i} tem {vowel} vogais')