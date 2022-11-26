#BIBLIOTECA OS

import os
"""
#getcwd -> onde o script está executando

ambiente = os.getcwd()
print(ambiente)

#listdir -> listar arquivos de uma pasta e não entra nas demais
print(os.listdir())

#walk -> lista separando em diretório e arquivo e entra nas pastas - precisa dizer onde começa (não executar no C: nem no desktop)
for i in os.walk("."):
    print(i)

#chdir -> troca o lugar onde seu script está sendo executado -cuidado com permissões
ambiente = os.getcwd()
print(ambiente)

os.chdir("projeto")

#mkdir -> criar pasta
os.mkdir("bin/arquivos")

#makedirs - criar pastas uma dentro da outra

#rmdir -> remover pasta vazia
os.rmdir("teste")

#removedirs -> remover pastas vazias
os.removedirs("teste/outroteste")

#PATH
#__file__ -> onde o script está instalado
print(__file__)

#basename -> nome base
base = os.path.basename(__file__)

print(base)
"""
#dirname -> diretorio base
dirn = os.path.dirname("usuarios.txt")
print(dirn)