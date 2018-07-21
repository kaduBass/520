#!  /usr/bin/python3
from pymongo import MongoClient
from random import randint
from bson.objectid import ObjectId

def insere ():
        nomes = ["jose","luciano","renato"]
        for u in nomes:
            idades=randint(78,112)
            el= {"nome":u,"idade":idades}
            insere=db.pessoas.insert(el)
    #for x in db.pessoas.find():
    #    print(x)
    #pra retornar a qtd de resultados usa-se len()
            doc = db.pessoas.find()
    #res = db.pessoas.count()#retorna a qtd de dict
   
            lista=[x for x in doc]
            #if u =="jose":
            #    remove = db.pessoas.remove({"nome":u})
    
def atualiza():
    db.pessoas.update({"_id":ObjectId("5b5346d4e3d0b51298eacf4e")},{"$set":{"nome":"schumacher"}})


try:
    client = MongoClient()
    db = client["4803"]
    
    total=db.pessoas.count()
    

except Exception as erro:
    print("nao conectou {} ".format(erro))