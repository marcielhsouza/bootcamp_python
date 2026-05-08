# 1) Solicita ao usuário que digite seu nome

nome = input("Digite o seu nome: ")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

sal = float(input("Digite o seu salario: "))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

bonus = float(input("Digite o bônus: "))

# 4) Calcule o valor do bônus final

sal_bonus =  1000 + sal * bonus   

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

print(f"O usuario {nome} com salario de {sal} com bônus de {bonus}, ele recebeu no total {sal_bonus}")


# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?