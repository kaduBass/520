#!  /usr/bin/python3

from funcoes import manipular_arquivo
#import funcoes
try:
    resultado=manipular_arquivo("regra.txt","r","#!  /usr/bin/python3\n")
    print(resultado)
except Exception as e:
    print(e)
    

