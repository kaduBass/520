#!  /usr/bin/python3
# introducao pyhton
#dicionario = {"nome":"carlos","sobrenome":"pantaleao"}
#dd=dicionario.get("giga","nao achei")
#for x , y  in dicionario.items():
#    print(x,y)
   
#print(dd)

frutas = [{"fruta":"uva","preco":3500,"qtd":10},{"fruta":"limao","preco":2700,"qtd":200}]

total=0
novoPrecoFrutas=[]
for fruta in frutas:
    
    preco=fruta["preco"] * 1.1
    re={"fruta":fruta["fruta"],"preco":round(preco)}
    novoPrecoFrutas.append(re)

#print("A quantidade gerada em vendas foi de R$ {} ,00".format(total))
print(novoPrecoFrutas)
    
#if ternario 
#nome="carlos"
#print("sim" if nome=="carlos" else "nao")
#print([lista.title() for lista in listas])
    