#Um programa que calcula o dobro, o triplo e a raiz quadrada de um número

n = int(input('Digite um número... '))

print('O numéro que você escolheu é {}, o seu dobro é {}, o triplo é {}, e a raiz quadrada {:.2f}.' .format(n,(n*2),(n*3),pow(n, (1/2))))