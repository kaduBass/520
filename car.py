#!  /usr/bin/python3
class CarTrack ():
    ''' especificacoes do carro'''
    def __init__(self):
        self.velocidade=300
        self.frenagem=100
        self.aceleracao=12
        self.peso=500
        self.multa=0
        self.desgaste_pneu=0
        self.combustivel=100
        self.destruicao=0
        self.tanque="litro"
        

    def vira_esquerda(self):

        if self.velocidade <=50:
            self.frenagem +=1

        elif self.velocidade >=50 and self.velocidade <=75:
            self.desgaste_pneu +=1
            self.bate()

        elif self.velocidade > 75 and self.velocidade <=100:
            self.desgaste_pneu +=2
            self.bate()
            self.bate()

        else:
            self.capota()

            

    def vira_direita(self):
        

    def capota(self):
        self.destruicao=100
        return "diminua sua velocidade na proxima vez , pra fazer a curva"

    def bate(self):
        self.destruicao +=1
        self.combustivel -=1
        self.multa=1000


    def subida(self):
        self.velocidade -=1
        self.desgaste_pneu -=1


    def descida(self):
        self.velocidade +=1
        self.desgaste_pneu +=1

    def trocar_pneu(self):
        self.desgaste_pneu=0


    def __str__(self):
        return("padrao da velocidade e {}".format(self.velocidade))

#from pai import CarTrack
class CarEletrico (CarTrack):
    def __init__(self,combustivel,velocidade,frenagem):
        super().__init__(combustivel,velocidade,frenagem)
        self.combustivel="energia"
        self.tanque="carga"
