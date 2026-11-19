ficheiro = open("auth.log", "r")
texto = ficheiro.read()
ficheiro.close()

sucessos= texto.count("Accepted password")

print("Logins com sucesso:", sucessos)