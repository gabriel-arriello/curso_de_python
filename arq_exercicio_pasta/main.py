
def bytes_to_megabytes(linha)
    pass

#Extração
arquivo = open("usuarios.txt", "r")
linhas = arquivo.readlines()
arquivo.close()


#Transformação
usuarios = {}

for linha in linhas:

    linha = linha.replace("\n", "")
    linha = linha.split("\t")

    usarios[linha(0)] = {
        "espaço": bytes_to_megabytes(linha[1])
    }