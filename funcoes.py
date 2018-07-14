#!  /usr/bin/python3
from random import choice
def abre():
    try:
        with open("erro.txt","r") as arquivo:
            lista=arquivo.readlines()
            return lista
    except Exception as erro:
        with open("erro.txt","w") as arquivo:
            arquivo.write("#!  /usr/bin/python3\n")
            return "criado"

def escopo():
    global x #atualiza a variavel global com o valor da variavel local
    x=8
    return x

def manipular_arquivo(nome,modo,conteudo=None,acesso=True):
    if modo =="r":
        try:
            with open(nome,modo) as arquivo:
                data=arquivo.readline()
                return data
        except Exception as erro:
            with open(nome,"w") as arq:
                arq.write(acesso)
                return "log criado no arquivo log.txt"

            return erro

    else:
        with open(nome,"w") as arquivo:
            arquivo.write(conteudo)
            return manipular_arquivo(nome,"r")


def forma(*apelido):
    print(apelido)



def frutas1(**fruta):#transforma os  parametros em dicinario
    ''' funcao de boas vindas '''#doc string e um comentario
    #for x in apelido.values():#values , keys, items
    #    print(x)
    produto=fruta["nome"]
    valor=fruta["valor"]
    qtd=fruta["qtd"]

    print("produto: {} , total:{}".format(produto,(valor * qtd)))


#frutas1(nome="uva",qtd=10,valor=75)

var = [lambda x: x.upper(),
lambda x : x.lower(),
lambda x :x.capitalize,
lambda x :x.title()
]
def mkl():
    with open("frutas1.txt","r") as arquivo:
        lista=arquivo.readlines()
        for x in lista:
            troca=x.replace("\n","")
            escolhe_funcao=choice(var)
            print(escolhe_funcao(troca))
        

#decordadores **********************************

def um():
    print("um")

def dois():
    print("dois")
    um()


def tres (retornoFuncao):
    def four():
        print(retornoFuncao())
        return retornoFuncao()
    return four()

#s@tres
def retornoFuncao():
    return "python"

def externa (idioma):
    dic={"pt":"ola","pi":"hi","en":"hello world"}
    def interna(nome):
        print("{} {}".format(dic[idioma],nome))
    return interna

#unc =externa("pt")#funcao externa
#func("pedro")#esta aqui e funcao interna
#func("carlos")
#func("eduardo")