pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)

pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)

pessoa["telefone"] = "3333-1234"                    # Adicionando a chave telefone no dict
print(pessoa)                                       # Mostra o dict pessoa {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}