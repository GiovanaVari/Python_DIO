contatos = {"guilherme@gmail.com": 
            {"nome": "Guilherme", 
             "telefone": "3333-2221"}}

resultado = contatos.pop("guilherme@gmail.com")         # Remove a chave informada
print(resultado)                                        # Mostra resultado               {'nome': 'Guilherme', 'telefone': '3333-2221'}

resultado = contatos.pop("guilherme@gmail.com", {})     # Busca se a chave informada existe em contatos, se nao existir retorna "{}"
print(resultado)                                        # Mostra resultado                ({})