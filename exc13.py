ficheiro = open("auth.log", "r")
texto = ficheiro.read()
ficheiro.close()

ip = input("Escreve um IP: ")

existe = ip in texto

print(existe)