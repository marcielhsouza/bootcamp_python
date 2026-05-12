# Strings (str)

#    Métodos e operações:
# .upper() (converte para maiúsculas)
nome = "marciel"
print(f"Sem .upper() = {nome}")
print(f"Com .upper() = {nome.upper()}")

#  .lower() (converte para minúsculas)
nome = "MARCIEL"
print(f"Sem .lower()  = {nome}")
print(f"Com .lower() = {nome.lower() }")

#  .strip() (remove espaços em branco no início e no final)
nome = "  MARCIEL  "
print(f"Sem .strip()  = {nome}")
print(f"Com .strip() = {nome.strip() }")

#  .split(sep) (divide a string em uma lista, utilizando sep como delimitador)
nome = "MAR/CIEL"
print(f"Sem .split()  = {nome}")
print(f"Com .split() = {nome.split(sep="/") }")

#  + (concatenação de strings)
