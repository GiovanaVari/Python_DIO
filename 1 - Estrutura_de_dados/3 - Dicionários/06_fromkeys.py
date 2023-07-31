resultado = dict.fromkeys(["nome", "telefone"])                 # Cria chaves vazias
print(resultado)                                                # Mostra o dict resultado                   {"nome": None, "telefone": None}

resultado = dict.fromkeys(["nome", "telefone"], "vazio")        # Cria chaves com o valor informado ("vazio") 
print(resultado)                                                # Mostra o dict resultado                   {"nome": "vazio", "telefone": "vazio"}