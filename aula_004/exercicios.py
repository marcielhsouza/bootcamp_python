# Exercícios de Listas e Dicionários

# 1) Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

# lista_num = list(range(1,11))

# for num in lista_num:
#     print(f"{num}² = {num**2} ")

# 2) Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

# linguagens = ["Python", "Java", "C++", "JavaScript"]
# print(linguagens)
# linguagens.remove("C++")
# print(linguagens)
# linguagens.append("Ruby")
# print(linguagens)

# 3) Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

# livro: dict = {'titulo': 'Harry Potter', 'autor': 'J.K Rolling', 'ano publicação': 2023}
# for chave, valor in livro.items():
#     print(f"n{chave}:{valor}")

# 4) Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.

    # 4.1) Possivel solução 

# texto: str = "otorrinolaringologista"
# cont_carateres: dict = {}
# for letra in texto:
#     if letra in cont_carateres:
#         cont_carateres[letra] += 1
#     else:
#         cont_carateres[letra] = 1
# print(cont_carateres)

    # 4.2) Possivel solução 

# texto: str = "otorrinolaringologista"
# cont_carateres: dict = {}
# for letra in texto:
#     cont_carateres[letra] = cont_carateres.get(letra,0) + 1
# print(cont_carateres)

# 5) Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

# lista_compra: list = ["maçã", "banana", "cereja"]
# valores_compra: dict = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}      
# total = sum([valores_compra[prod] for prod in lista_compra])
# print(total)

# Exercícios intermediários e mais avançados

# 6) Eliminação de Duplicatas

#Objetivo: Dada uma lista de emails, remover todos os duplicados.
emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
emails_unicos = set(emails)
print(emails_unicos)

# 7) Filtragem de Dados

# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

# idades = [22, 15, 30, 17, 18]
# idades_validas = [idade for idade in idades if idade >= 18]

# print(idades_validas)

# 8) Ordenação Personalizada

# Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

# pessoas = [
#     {"nome": "Alice", "idade": 30},
#     {"nome": "Bob", "idade": 25},
#     {"nome": "Carol", "idade": 20}
# ]
# pessoas.sort(key=lambda pessoa: pessoa["nome"])

# print(pessoas)

# 9) Agregação de Dados

# Objetivo: Dado um conjunto de números, calcular a média.

# numeros = [10, 20, 30, 40, 50]
# media = sum(numeros) / len(numeros)

# print("Média:", media)

# 10) Divisão de Dados em Grupos

# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

# valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# pares = [valor for valor in valores if valor % 2 == 0]
# impares = [valor for valor in valores if valor % 2 != 0]

# print("Pares:", pares)
# print("Ímpares:", impares)

# Exercícios com Dicionários

# 11) Atualização de Dados

# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

# produtos = [
#     {"id": 1, "nome": "Teclado", "preço": 100},
#     {"id": 2, "nome": "Mouse", "preço": 80},
#     {"id": 3, "nome": "Monitor", "preço": 300}
# ]

# # Atualizar o preço do produto com id 2 para 90
# for produto in produtos:
#     if produto["id"] == 2:
#         produto["preço"] = 90

# print(produtos)

# 12) Fusão de Dicionários

# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.

# dicionario1 = {"a": 1, "b": 2}
# dicionario2 = {"c": 3, "d": 4}

# dicionario_fundido = {**dicionario1, **dicionario2}

# print(dicionario_fundido)

# 13) Filtragem de Dados em Dicionário

# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

# estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

# estoque_positivo = {produto: quantidade for produto, quantidade in estoque.items() if quantidade > 0}

# print(estoque_positivo)

# 14) Extração de Chaves e Valores

# Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.

# dicionario = {"a": 1, "b": 2, "c": 3}
# chaves = list(dicionario.keys())
# valores = list(dicionario.values())

# print("Chaves:", chaves)
# print("Valores:", valores)

# 15) Contagem de Frequência de Itens

# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.

# texto = "engenharia de dados"
# frequencia = {}

# for caractere in texto:
#     if caractere in frequencia:
#         frequencia[caractere] += 1
#     else:
#         frequencia[caractere] = 1

# print(frequencia)