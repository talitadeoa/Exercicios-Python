#Um programa que aplica uma multa caso ultrapasse a velocidade máxima e calcula a multa por R$7 a cada km excedente

velocidade = int(input("Qual a velocidade em Km/h? "))
velocidade_maxima = 80
excedente = velocidade-velocidade_maxima
multa = excedente*7

if velocidade > velocidade_maxima:
    print("Você excedeu o limite de {}Km/h!".format(velocidade_maxima))
    print("Sua multa é de R${:.2f}".format(multa))
else:
    print("Sua velocidade está ideal, siga dirigindo! =D")

    



