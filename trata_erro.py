#!  /usr/bin/python3
try:
    with open("erro.txt","r") as arquivo:
        lista=arquivo.readlines()
       
except Exception as erro:
    with open("erro.txt","w") as arquivo:
        arquivo.write("#!  /usr/bin/python3\n")
    