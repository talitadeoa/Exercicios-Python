#Um programa que calcula a quantidade de tinta necessária para pintar uma parede

altura = float(input('Qual a altura da parede em metros? '))
largura = float(input('Qual a largura da parede em metros? '))

area = altura*largura
tinta = area/2

#colocar mais print com infos

print('Serão necessários {:.3} litros de tinta' .format(tinta))