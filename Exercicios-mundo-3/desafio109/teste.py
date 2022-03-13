
import moeda

p = float(input('Digite o preço: R$'))

print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p,True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p,True)}')
print(f'Aumentado 13% de {moeda.moeda(p)}, temos {moeda.aumentar(p,13,True)}')
print(f'Diminuindo 14% de {moeda.moeda(p)}, temos {moeda.diminuir(p,14,True)}')