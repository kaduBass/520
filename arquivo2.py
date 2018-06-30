#!  /usr/bin/python3
# introducao pyhton
#arquivo = open("git.txt","r")
#print(arquivo.read())
#arquivo.close()

#outra maniera de abrir um arquivo melhor opcao


with open("frutas1.txt","r") as arquivo:
    conteudo = arquivo.readlines()
with open("frutas2.txt","w") as arquivo:
    cont=1
    for li in conteudo :
        print(li.replace("\n","-{}\n".format(cont)))
        cont +=1
           
    