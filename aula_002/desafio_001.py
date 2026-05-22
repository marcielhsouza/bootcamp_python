# Solicita ao usuário que digite seu nome
try:
    nome = input("Digite seu nome: ")
        # Verifica se o nome está vazio
    if len(nome)==0:
        raise ValueError("O nome não pode estar vazio.")
    elif any(char.isdigit() for char in nome):
        raise ValueError("O nome não deve conter números.")
    else:
        print(f"Nome válido: {nome}")
except ValueError as e:
    print(e)
    exit()
    
# Solicita ao usuário que digite o valor do seu salário e converte para float
try:
    salario = float(input("Digite o valor do seu salário: "))
    if salario <0:    
        print("Por favor, digite um valor positivo para o salário.")
except ValueError as e:
    print("Entrada inválida para o salário. Por favor, digite um número.")
    exit()

# Solicita ao usuário que digite o valor do bônus recebido e converte para float
try:
    bonus = float(input("Digite o bônus do seu salário: "))
    if bonus <0:    
        print("Por favor, digite um valor positivo para o bônus.")
except:
    print("Entrada inválida para o bônus. Por favor, digite um número.")
    exit()

# Assumindo uma lógica de cálculo para o bônus final e KPI
bonus_final = 1000 + (salario * bonus)
kpi = (salario + bonus_final) / 1000

# Imprime as informações para o usuário
print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_final:.2f}.")

