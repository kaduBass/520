#!  /usr/bin/python3
# introducao pyhton

with open("frutas4.txt","w") as arquivo:
    while True:
        nome=input("Digite um nome")
        if nome =="sair":
            break
        arquivo.write("{}\n".format(nome))
