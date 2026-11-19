ficheiro = open("auth.log", "r")
texto = ficheiro.read()
ficheiro.close()

ip = input("Introduza um IP: ")
quantidade = texto.count(ip)

print(f"O IP {ip} aparece {quantidade} vezes.")

relatorio = open("relatorio.txt", "a")
relatorio.write(f"Pesquisa do IP {ip}: {quantidade} ocorrências\n")
relatorio.close()