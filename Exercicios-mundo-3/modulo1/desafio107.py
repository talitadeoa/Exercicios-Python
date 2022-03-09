
import moeda

p = float(input('Digite o preço: R$'))

print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentado 13% de {p}, temos {moeda.aumentar(p,13)}')
print(f'Diminuindo 14% de {p}, temos {moeda.diminuir(p,14)}')