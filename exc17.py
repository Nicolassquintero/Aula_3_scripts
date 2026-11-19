ficheiro = open("auth.log", "r")
texto = ficheiro.read()
ficheiro.close()

quantidade = texto.count("61.177.173.22")

print("Ocorrências do IP 61.177.173.22:", quantidade)