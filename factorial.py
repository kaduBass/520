#!  /usr/bin/python3

def fatorial(num):
    aux=1
    for x in range(1, num+1):
        aux*=x
    return aux
        
print(fatorial(78))

