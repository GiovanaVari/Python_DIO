linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()                                           # ordena alfabeticamente (["c", "csharp", "java", "js", "python"])
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]        
linguagens.sort(reverse=True)                               # inverte a ordem alfabetica (["python", "js", "java", "csharp", "c"])
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]        
linguagens.sort(key=lambda x: len(x))                       # ordena por tamanho (["c", "js", "java", "python", "csharp"])
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)         # ordena por tamanho e inverte (["python", "csharp", "java", "js", "c"])
print(linguagens)