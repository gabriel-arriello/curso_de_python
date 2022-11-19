arquivo_ips = open("arquivo_ips.txt", "r")
linhas_ips = arquivo_ips.readlines()

validos = []
invalidos = []

for ip in linhas_ips:
    ip = ip.replace("\n", "")
    apoio = ip.split(".")

    apoio = [a for a in apoio if int(a) <= 255]
    if len(apoio) == 4:
        validos.append(ip)
    else:
        invalidos.append(ip)

saida = open("saida.txt", "w")
saida.write("[Endereços válidos:]\n")
for v in validos:
    saida.write(f"{v}\n")

saida.write("[Endereços inválidos:]\n")
for i in invalidos:
    saida.write(f"{i}\n")