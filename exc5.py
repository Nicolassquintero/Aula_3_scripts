ficheiro = open("auth.log", "r")
texto = ficheiro.read()
ficheiro.close()

falhas = texto.count("Failed password")

print("Tentativas falhadas:", falhas)