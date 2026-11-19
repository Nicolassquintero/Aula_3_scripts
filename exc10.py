ficheiro = open("auth.log", "r")
texto = ficheiro.read()
ficheiro.close()

vitor = texto.count("vitor")

print("Ocorrências de vitor:", vitor)