contato = {"nome": "Guilherme", "telefone": "3333-2221"}

contato.setdefault("nome", "Giovanna")  # Se existir no dict retorna o valor, se nao adiciona           "Guilherme"
print(contato)                          # {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("idade", 28)         # 28
print(contato)                          # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}