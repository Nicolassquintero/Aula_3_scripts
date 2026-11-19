ficheiro = open("auth.log", "r")
texto = ficheiro.read()
ficheiro.close()

existe = "Failed password" in texto

print(existe)