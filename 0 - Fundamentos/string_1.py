nome = "gioVana"

print(nome.upper())                         # todos os caracteres MAIUSCULOS
print(nome.lower())                         # todos os caracteres minusculos
print(nome.title())                         # estilo titulo ex. Giovana

texto = "  Olá mundo!       "

print(texto + ".")
print(texto.strip() + ".")                  # tira espaços em branco da direita e esquerda
print(texto.rstrip() + ".")                 # tira espaços em branco da esquerda
print(texto.lstrip() + ".")                 # tira espaços em branco da direita

menu = "Python"

print("****" + menu + "****")
print(menu.center(14))                      # centraliza e de acordo com o número passado preenche com o passado depois do número (espaço em branco)
print(menu.center(14 , "#"))                # centraliza e de acordo com o número passado preenche com o passado depois do número
print(menu.center(14 , "*"))                # centraliza e de acordo com o número passado preenche com o passado depois do número
print("*".join(menu))                       # separa as letras colocando o que foi passado
print(".".join(menu))                       # separa as letras colocando o "."