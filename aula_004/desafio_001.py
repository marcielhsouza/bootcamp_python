#Integre na solução anterior um fluxo de While que repita o fluxo até que o usuário insira as informações corretas




# Solicita ao usuário que digite seu nome

def salario_bonus():

    nome_valido = False
    salario_valido = False
    bonus_valido = False

    while nome_valido is not True:
        try:
            nome = input("Digite seu nome: ")
                # Verifica se o nome está vazio
            if len(nome)==0:
                raise ValueError("O nome não pode estar vazio.")
            elif nome.isdigit():
                raise ValueError("O nome não deve conter números.")
            elif nome.isspace():
                raise ValueError("O nome não pode estar vazio.")
            else:
                nome_valido = True
        except ValueError as e:
            print(e)

    # Solicita ao usuário que digite o valor do seu salário e converte para float

    while salario_valido is not True:
        try:
            salario = float(input("Digite o valor do seu salário: "))
            if salario <0:    
                raise ValueError("Por favor, digite um valor positivo para o salário.")
            else:
                salario_valido = True
        except ValueError as e:
            print("Entrada inválida para o salário. Por favor, digite um número.")


    # Solicita ao usuário que digite o valor do bônus recebido e converte para float

    while bonus_valido is not True:
        try:
            bonus = float(input("Digite o bônus do seu salário: "))
            if bonus <0:    
               raise ValueError("Por favor, digite um valor positivo para o bônus.")
            else:
                bonus_valido = True
        except ValueError as e:
            print("Entrada inválida para o bônus. Por favor, digite um número.")

    # Assumindo uma lógica de cálculo para o bônus final e KPI
    bonus_final = 1000 + (salario * bonus)
    kpi = (salario + bonus_final) / 1000

    # Imprime as informações para o usuário
    print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_final:.2f}.")

    return nome, salario, bonus_final

salario_bonus()