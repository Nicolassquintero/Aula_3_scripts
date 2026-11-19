ficheiro = open("auth.log", "r")
texto = ficheiro.read()
ficheiro.close()

invalidos = texto.count("invalid user")

print("Tentativas com utilizadores inexistentes:", invalidos)