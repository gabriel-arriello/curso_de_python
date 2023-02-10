

arq_mb = float(input("Insira o tamanho do arquivo em MB: "))
internet_mpbs = float(input("Insira a velocidade do link de internet em Mbps: "))

tempo_download = arq_mb / internet_mpbs

print(f"Tempo aproximado de download: {tempo_download} segundos.")

