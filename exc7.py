ficheiro = open("auth.log", "r")
texto = ficheiro.read()
ficheiro.close()

linhas = texto.count("\n")

print("Número de linhas:", linhas)