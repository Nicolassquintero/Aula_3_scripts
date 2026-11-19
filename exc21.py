ficheiro = open("auth.log", "r")
texto = ficheiro.read()
ficheiro.close()

falhas = texto.count("Failed password")
sucessos = texto.count("Accepted password")
linhas = texto.count("\n")

if linhas > 0:
    taxa = falhas / linhas * 100
else:
    taxa = 0

relatorio = open("relatorio.txt", "w")

relatorio.write("RELATORIO DE AUTENTICAÇAO\n")
relatorio.write("=" * 30 + "\n")
relatorio.write(f"Tentativas falhadas: {falhas}\n")
relatorio.write(f"Logins com sucesso: {sucessos}\n")
relatorio.write(f"Total de linhas: {linhas}\n")
relatorio.write(f"Taxa de falha: {taxa:.2f}%\n")

relatorio.close()

print("Relatório guardado em relatorio.txt")