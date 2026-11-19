ficheiro = open("auth.log", "r")
texto = ficheiro.read()
ficheiro.close()

ip1 = "61.177.173.22"
ip2 = "193.168.1.45"
ip3 = "222.186.42.7"
ip4 = "45.148.10.3"

ataques1 = texto.count(ip1)
ataques2 = texto.count(ip2)
ataques3 = texto.count(ip3)
ataques4 = texto.count(ip4)

relatorio = open("relatorio.txt", "a")

relatorio.write("\nATAQUES POR IP\n")
relatorio.write("=" * 30 + "\n")

relatorio.write(f"IP {ip1}: {ataques1} ataques\n")
relatorio.write(f"IP {ip2}: {ataques2} ataques\n")
relatorio.write(f"IP {ip3}: {ataques3} ataques\n")
relatorio.write(f"IP {ip4}: {ataques4} ataques\n")

relatorio.close()

print("Relatório atualizado.")