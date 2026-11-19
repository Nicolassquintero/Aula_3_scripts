ficheiro = open("auth.log", "r")
texto = ficheiro.read()
ficheiro.close()

falhas = texto.count("Failed password")
sucessos = texto.count("Accepted password")
linhas = texto.count("\n")

relatorio = open("relatorio.txt", "w")

relatorio.write("RELATORIO DE AUTENTICACAO\n")
relatorio.write("=" * 30 + "\n")
relatorio.write(f"Tentativas falhadas: {falhas}\n")
relatorio.write(f"Logins com sucesso: {sucessos}\n")
relatorio.write(f"Total de linhas: {linhas}\n")

relatorio.close()