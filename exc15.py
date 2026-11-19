ficheiro = open("auth.log", "r")
texto = ficheiro.read()
ficheiro.close()

minuscula = texto.count("failed")
maiuscula = texto.count("Failed")

print("Ocorrências de failed:", minuscula)
print("Ocorrências de Failed:", maiuscula)

# A diferençã esta em a primeira letra (F,f)