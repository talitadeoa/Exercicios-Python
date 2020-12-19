#Um programa que lê um número e mostra cada um separadamente

n = int(input('Digite um número... '))

print("""
unidade = {}
dezena = {}
centena = {}
milhar = {}""".format(n//1%10,n//10%10,n//100%10,n//1000%10))