ficheiro = open("auth.log", "r")
texto = ficheiro.read()
ficheiro.close()

quantidade = len(texto)

print("Número de caracteres:", quantidade)