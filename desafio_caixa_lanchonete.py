valorHamburguer = float(input("Valor do Hamburguer? "))
quantidadeHamburguer = int(input("Quantidade de Hamburguer? "))
valorBebida = float(input("Valor da bebida? "))
quantidadeBebida = int(input("Quantidade de bebida? "))
valorPago = float(input("Valor pago? "))

total = (quantidadeHamburguer * valorHamburguer) + (quantidadeBebida * valorBebida)
troco = valorPago - total

mensagem = f"O preço final do pedido é R$ {total:.2f}. Seu troco é R$ {troco:.2f}."
print(mensagem)
