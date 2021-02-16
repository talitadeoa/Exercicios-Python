#Um programa que informas quantas vogais tem cada palavraa de uma tupla

words = ('pao', 'feijao', 'macarrao', 'sal', 'suco', 'arroz')
vowel = ['a','e','i','o','u']

for word in words:
    print(f'\nA palavra {word.u} tem as vogais: ', end='')
    for i in word:
        if i.lower() in vowel:
            print(i, end=' ')