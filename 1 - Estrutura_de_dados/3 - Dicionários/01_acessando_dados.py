dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}         # Criando o dict

print(dados["nome"])                                                        # Mostra o que esta na chave informada "Guilherme"
print(dados["idade"])                                                       # Mostra o que esta na chave informada 28
print(dados["telefone"])                                                    # Mostra o que esta na chave informada "3333-1234"

dados["nome"] = "Maria"                                                     # Atribuindo novo valor a chave informada
dados["idade"] = 18                                                         # Atribuindo novo valor a chave informada
dados["telefone"] = "9988-1781"                                             # Atribuindo novo valor a chave informada

print(dados)                                                                # Mostra o dict todo {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}