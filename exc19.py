ficheiro = open("auth.log", "r")
texto = ficheiro.read()
ficheiro.close()

sucessos = texto.count("Accepted password")
linhas = texto.count("\n")

relatorio = open("relatorio.txt", "a")
relatorio.write(f"Logins com sucesso: {sucessos}\n")
relatorio.write(f"Total de linhas: {linhas}\n")
relatorio.close()