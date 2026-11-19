ficheiro = open("auth.log", "r")
texto = ficheiro.read()
ficheiro.close()

existe = "8.8.8.8" in texto

print(existe)