# Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. 
# O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.

nome = input("Digite o seu nome: ")
sal_mensal = float(input("Digite o valor do seu salario mensal: "))
sal_bonus = float(input("Digite o valor do bônus: "))

bonus = 1000 + sal_mensal * sal_bonus

print("Olá", nome, "seu bônus é de", bonus)