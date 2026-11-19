ficheiro = open("auth.log", "r")
texto = ficheiro.read()
ficheiro.close()

minuscula = texto.lower()
quantidade = minuscula.count("failed")


print("Ocorrências de failed:", quantidade)
