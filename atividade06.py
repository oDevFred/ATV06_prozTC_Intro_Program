# Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
# A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

# Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.

# Enquanto tiver rodando
while True:
    # Tente
    try:
        # Declarando variáveis
        nome        = input('Digite seu nome completo: ');
        ano_nasc    = int(input('Digite seu ano de nascimento (1922 - 2021): '));
        # Calculando idade
        idade       = 2022 - ano_nasc;

        # Se o ano de nascimento for menor que 1922 ou maior que 2021
        if ano_nasc < 1922 or ano_nasc > 2021:
            # Informe o erro e reinicie o programa
            raise Exception('Por favor, digite um ano de nascimento entre 1922 e 2021.');

        # Informe o nome e a idade em 2022
        print(f'Seu nome é {nome} e você tem {idade} anos.');
        break; # Termine o código
    
    # Se caso houve um erro, coloque em 'e'
    except Exception as e:
        # Informe o erro
        print(e);