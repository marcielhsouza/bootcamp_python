# Type Hint

idade: int = 8
altura: float = 1.75
nome: str = "Alice"
is_estudante: bool = True

# Lista e Dicionários

#Lista 

lista: list = ["Sapato",39, 10.38, True]
print(lista)

#Dicionario

produto_01: dict = {"nome":"sapato","quantidade":39, "preco":10.38,"disponibilidade":True}
produto_02: dict = {"nome":"Televisão","quantidade":10, "preco":910.38,"disponibilidade":True}

carrinho: list = []
carrinho.append(produto_01)
carrinho.append(produto_02)

print(carrinho)