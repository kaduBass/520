#!  /usr/bin/python3
# introducao pyhton
#arquivo = open("git.txt","r")
#print(arquivo.read())
#arquivo.close()

#outra maniera de abrir um arquivo melhor opcao
with open ("frutas1.txt","a") as f:
    #print(f.readline(),end = "")#retorna as linhas em lista
    #print(f.readline(),end = "")#retorna as linhas em lista
    #f.seek(0)#zera o cursor
    #print(f.readline(),end = "")#retorna as linhas em lista
    listas = ["limao","uva","maca"]
    i=0
    for lista in listas:
        i+=1
        f.write("{}- {} \n".format(i,lista))
        with open ("frutas1.txt","r") as g:
            dados=(g.readlines())

with open("frutas1.txt","r") as arquivo1:
    conteudo = arquivo1.readlines()

           
    