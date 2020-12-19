#Um algoritimo que lê um valor em metros e converte para centímetros e milímetros

metro = float(input('Digite um valor em metro... '))

quilômetros = metro/1000 
hectômetros = metro/100
decâmetros = metro/10
decímetros = metro*10
centímetros = metro*100
milímetros = metro*1000

print(' \n {:.0f} metros equivale a: \n {} quilômetros \n {} hectômetros \n {} decâmetros \n {:.0f} decímetros \n {:.0f} centímetros \n {:.0f} milímetros' 
.format(metro,(metro/1000),(metro/100),(metro/10),(metro*10),(metro*100),(metro*1000)))