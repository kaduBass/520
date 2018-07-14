#!  /usr/bin/python3

from datetime import datetime
from funcoes import manipular_arquivo

while True:
    s=input("digite o nome do arquivo s =sair")
    if s=="s":
        break
    modo=input("modo de abrir o arquivo")
    if modo=="r":
        a=manipular_arquivo(s,modo,datetime.now())
        print(a)
    elif modo=="a":
        conteudo=input("digite o conteudo")
        manipular_arquivo(s,modo,conteudo+"\n")


