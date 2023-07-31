contatos = {                                                                  #Criando dict com dict em cada chave
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

telefone = contatos["giovanna@gmail.com"]["telefone"]                         # Atribui a telefone o valor referente ao telefone que esta vinculado ao contato informado
print(telefone)                                                               # Mostra o que esta em telefone      ("3443-2121")