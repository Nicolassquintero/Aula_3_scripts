ficheiro = open("auth.log", "r")
texto = ficheiro.read()
ficheiro.close()

palavra = input("Escreve uma palavra: ")

quantidade = texto.count(palavra)

print(quantidade)