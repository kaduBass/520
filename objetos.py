#!  /usr/bin/python3
class Pessoa ():
    def __init__(self,nome="antonio",idade=134,cabelo="branco",energia=50,fome=2,pulos=60,tiros):
        self.nome=nome
        self.idade=idade
        self.cabelo=cabelo
        self.energia=energia
        self.fome=fome
        self.pulos=pulos
        self.tiros=15
    
    def correr(self):
        self.energia -=1
        self.fome -=1
        #print ("correr com energia {} . Com fome de {}".format(self.energia,self.fome))
        

    def dormir(self):
        self.energia=5
        self.fome=5
        return ("energia e de {} e a fome e de {}".format(self.energia,self.fome))

    def andar(self):
        self.energia=3
        return ("andar")

    def pular(self):
        self.pulos=15

    def atirar_pulando(self):
        self.tiro=34

    def __str__(self):
        return "".format(self.fome)

   





