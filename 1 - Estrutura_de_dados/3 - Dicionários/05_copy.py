contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

copia = contatos.copy()                                                                 # Copiando o dict contatos para copia
copia["guilherme@gmail.com"] = {"nome": "Gui"}

print(contatos["guilherme@gmail.com"])                                                  # Mostra o dict contatos com a chave informada {"nome": "Guilherme", "telefone": "3333-2221"}

print(copia["guilherme@gmail.com"])                                                     # Mostra o dict copia com a chave informada {"nome": "Gui"}