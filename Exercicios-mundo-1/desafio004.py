#Um programa que mostra varias informações sobre o valor de uma variavel

c = input('Digite algo... ')  

print("""O tipo primitivo desse valor é {}
    Esse valor só tem espaços? {}
    Esse valor é um número? {}
    Esse valor é uma letra? {}
    Esse valor é alfanumérico? {}
    Esse valor está em letra maiúscula? {}
    Esse valor está em letra minuscula? {}""".format(type(c),c.isspace(),c.isnumeric(),c.isalpha(),c.islower(),c.isalnum(),c.isupper()))
