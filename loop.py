#!  /usr/bin/python3
# introducao pyhton

#numeros =[0,1,2,3,4,5,6,7,8,9]

#lista = list(range(0,50,3))

#print(lista)
#print(cpia)
#num = int (input("digite o numero"))
soma=0
#for x in range(6):
    #num = int(input("a nota é {}".format(x+1)))
    #soma += num

#media = soma / 6

fase = 25
bloco = fase >=23 and fase <=26

if bloco:
    nomes=[]
    while True:
        nome = input("ola digite seu nome")
        if nome == "carlos":
            break
        nomes.append(nome)
    for x in nomes:
        if x == "yahoo":
            print("encontrei yahoo")
            break
    else:
        print("nao encontrei")               
else:
    print("nao")


