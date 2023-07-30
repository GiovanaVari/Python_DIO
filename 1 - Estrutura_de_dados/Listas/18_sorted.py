linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))                     # Função para ordenar alfabeticamente a lista (["c", "js", "java", "python", "csharp"])
print(sorted(linguagens, key=lambda x: len(x), reverse=True))       # Função para ordenar alfabeticamente a lista e inverter (["python", "csharp", "java", "js", "c"])