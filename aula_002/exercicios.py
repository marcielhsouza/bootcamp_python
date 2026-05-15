# Inteiros (int)

# 001 - Escreva um programa que soma dois números inteiros inseridos pelo usuário.

# num1 = int(input("Insira o primeiro número: "))
# num2 = int(input("Insira o segundo número: "))
# soma = num1 + num2
# print(f"A soma dos dois números digitados pelo usuário é: {soma}")

# 002 - Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

# num = int(input("Insira um número: "))
# resto_resultado = num % 5 
# print(f"O resto da divisão por 5 é: {resto_resultado}")

# 003 - Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

# num1 = int(input("Insira o primeiro número: "))
# num2 = int(input("Insira o segundo número: "))
# multiplicacao = num1 * num2
# print(f"A multiplicação dos dois números digitados pelo usuário é: {multiplicacao}")

# 004 - Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

# num1 = int(input("Insira o primeiro número: "))
# num2 = int(input("Insira o segundo número: "))
# divisao = num1 / num2
# print(f"A divisão inteira dos dois números digitados pelo usuário é: {divisao}")

# 005 - Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# num1 = int(input("Insira um que deseja elevar ao quadrado número: "))
# quadrado = num1 ** 2
# print(f"A o resultado de {num1} elevado a 2 é: {quadrado}")

# Números de Ponto Flutuante (float)

# 006 - Escreva um programa que receba dois números flutuantes e realize sua adição.

# num1 = float(input("Insira o primeiro número: "))
# num2 = float(input("Insira o segundo número: "))
# soma = num1 + num2
# print(f"A soma dos dois números do tipo float digitados pelo usuário é: {soma}")

# 007 - Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

# num1 = float(input("Insira o primeiro número: "))
# num2 = float(input("Insira o segundo número: "))
# media = (num1 + num2) / 2
# print(f"A média dos dois números do tipo float digitados pelo usuário é: {media}")

# 008 - Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

# num1 = float(input("Insira o primeiro número (base): "))
# num2 = float(input("Insira o segundo número (expoente): "))
# potencia = num1 ** num2
# print(f"O resultado da exponenciação do números do tipo float digitados pelo usuário é: {potencia}")

# 009 - Faça um programa que converta a temperatura de Celsius para Fahrenheit.

# temp_celcius = float(input("Digite a temperatura (Celsius): "))
# fahrenheit = (temp_celcius * 1.8) + 32
# print(f"A temperatura digitada (Celsius) é de {fahrenheit} em Fahrenheit")

# 010 - Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# raio = float(input("Digite o raio do circulo: "))
# area_circ = 3.14 * (raio**2)
# print(f"A área to circulo é de : {area_circ}")

# Strings (str)

# 011 - Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

# palavra = input("Digite uma plavra que deseja tranforma em maiúscula: ")
# palavra_maiuscula = palavra.upper()
# print(f"A palavra digitada em letras maiúsculas: {palavra_maiuscula}")

# 012 - Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

# nome = input("Digite seu nome completo: ")
# nome_minusculo = nome.lower()
# print(f"A o nome completo em minusculo é: {nome_minusculo}")

# 013 - Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

# frase = input("Insira uma frase: ")
# frase_strip = frase.strip()
# print(f"A frase digitada sem espaços (incio e fim): {frase_strip}")

# 014 - Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

# data = input("Insira uma data (dd/mm/aaaa): ")
# data_sep = data.split('/')
# print(f"Data digitada: {data}")
# print(f"Dia: {data_sep[0]}")
# print(f"Mês: {data_sep[1]}")
# print(f"Ano: {data_sep[2]}")

# 015 - Escreva um programa que concatene duas strings fornecidas pelo usuário.

# primeiro_nome = input("Digite o priemiro nome: ")
# segundo_mome = input("Digite o segundo nome: ")
# nome_sobrenome = primeiro_nome + ' ' +segundo_mome
# print(f"O nome completo é: {nome_sobrenome}")

# Booleanos (bool)

# 016 - Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

# valor_bool1 = True
# valor_bool2 = True
# result_bool = valor_bool1 and valor_bool2
# print(f"O resultado da expressão booleana 'AND' entre dois valores é: {result_bool}")

# 017 - Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

# valor_bool1 = False
# valor_bool2 = False
# result_bool = valor_bool1 or valor_bool2
# print(f"O resultado da expressão booleana 'OR' entre dois valores é: {result_bool}")

# 018 - Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

# valor_bool1 = True
# result_not = not valor_bool1
# print(f"O resultado da expressão booleana 'NOT' é: {result_not}")

# 019 - Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

# valor_bool1 = 10
# valor_bool2 = 5
# result_igual = valor_bool1 == valor_bool2
# print(f"O resultado da expressão booleana '==' entre dois valores é: {result_igual}")

# 020 - Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.]

# valor_bool1 = 10
# valor_bool2 = 10
# result_dif = valor_bool1 != valor_bool2
# print(f"O resultado da expressão booleana '!=' entre dois valores é: {result_dif}")

# 021 - Conversor de Temperatura
# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, 
# garantir que a entrada seja numérica, tratando qualquer ValueError. 
# Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

try:
   temp_celcius = float(input("Digite a temperatura (Celsius): "))
   fahrenheit = (temp_celcius * 1.8) + 32
   print(f"A temperatura digitada (Celsius) é de {fahrenheit} em Fahrenheit")
except ValueError as e:
    print("Digite um número válido.")

# 022 - Verificador de Palíndromo 
# Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). 
# Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.

# 023 - Calculadora Simples 
# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. 
# Use try-except para lidar com divisões por zero e entradas não numéricas. Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. 
# Imprima o resultado ou uma mensagem de erro apropriada.

# 024 - Classificador de Números 
# Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para 
# classificar o número como "positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".

# 025 - Conversão de Tipo com Validação 
# Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve converter a string de entrada em uma lista de números inteiros. Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.
