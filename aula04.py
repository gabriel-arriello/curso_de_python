
#ARQUIVOS - dois tipos
#Texto - plein text
#Binário

#Função: Open - leitura (read), escrita (write) ou acrescentar (append)
#Após utilizado: SEMPRE lembrar de fechar

#BINÁRIO - STREAMING
#DUAS PARTES IMPORTANTES: ID (início, tipo de arquivo) - EOF (final, determina o fim da leitura)


#OPEN - É abrir e ler (tipo dois cliques)
#Primeiro parâmetro: nome do arquivo
#Segundo parâmetro: modo de abertura


#MODO "r" - só leitura
arquivo = open("meuarquivo.txt", "r")

#READ (para arquivos pequenos, pois abre inteiro e a máquina precisa suportar)
#- Para ler meu arquivo como string

arquivo = open("meuarquivo.txt", "r")
conteudo = arquivo.read()

#- Para ler meu arquivo como lista (cada elemento uma linha)

arquivo = open("meuarquivo.txt", "r")
conteudo = arquivo.readlines()

#CLOSE - sempre (já escreve junto com o open e faz o cógido no meio)
arquivo = open("meuarquivo.txt", "r")
arquivo.close()


#MODO "w" - criar um arquivo para escrever na pasta que está desenvolvendo
#se não existir, cria
#se existir, substitui (apaga TUDO e não tem volta)
#se aberto, não pode ser lido

arquivo = open("meuarquivo.txt", "w")

#WRITE (escrever seu arquivo)
#- Para inserir sua string no arquivo

arquivo = open("meuarquivo.txt", "r")
conteudo = arquivo.write()
arquivo.close()


#MODO "a" - acrescentar texto no fim do arquivo
arquivo = open("meuarquivo.txt", "a")

arquivo.write ("\nEu sou lindo\n")

#MUDAR ALGO NO MEIO DO ARQUIVO - muito complexo
#Ler, encontrar exatamente o local (seek), alterar e reescrever
#Nem pensar nisso por enquanto


#BIBLIOTECA OS
#permite utilizar operações básicas no sistema operacional onde o script está sendo executado
#criar, deletar, modificar e navegar em arquivos e pastas
#pathlib

import os
ambiente = os.getcwd()

ambiente = os.listdir()



#EXERCÍCIO

