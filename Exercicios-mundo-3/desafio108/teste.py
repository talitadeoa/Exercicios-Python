
import moeda

p = float(input('Digite o preço: R$'))

print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentado 13% de {moeda.moeda(p)}, temos {moeda.moeda(moeda.aumentar(p,13))}')
print(f'Diminuindo 14% de {moeda.moeda(p)}, temos {moeda.moeda(moeda.diminuir(p,14))}')