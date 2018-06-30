#!  /usr/bin/python3
par,impar,tudo=[],[],[]
for gera in range(1,21):
    tudo.append(gera)
    if gera %2 ==0:
        par.append(gera)
    else:
        impar.append(gera)
print(tudo)
print(par)
print(impar)  