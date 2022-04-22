def ler_dinheiro(prompt):
    while True:
        x = input(prompt).replace(',', '.').strip()
        if x.isdigit() or x.replace('.', '',1).isdigit():
            return float(x)
        else: 
            print(f'ERRO: "{x}" é um preço inválido!')