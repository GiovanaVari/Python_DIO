contatos = {"guilherme@gmail.com": 
            {"nome": "Guilherme", 
             "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError

resultado = contatos.get("chave")               # Busca se a chave informada existe em contatos                                     (None)
print(resultado)

resultado = contatos.get("chave", {})           # Busca se a chave informada existe em contatos, se nao existir retorna "{}"        ({})
print(resultado)

resultado = contatos.get(                       # Busca se a chave informada existe em contatos, se nao existir retorna "{}"
    "guilherme@gmail.com", {}
)                                               # Mostra o que esta em resultado                                                    {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
print(resultado)