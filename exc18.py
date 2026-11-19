ficheiro = open("auth.log", "r")
texto = ficheiro.read()
ficheiro.close()

falhas = texto.count("Failed password")

relatorio = open("relatorio.txt", "w")
relatorio.write(f"Tentativas falhadas: {falhas}\n")
relatorio.close()