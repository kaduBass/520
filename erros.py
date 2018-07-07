#!  /usr/bin/python3
#quando encontrar erro nao para o script 
try:
    num1=int(input("digite um numero"))
    num2=(input("digite um numero"))
    divide=num1+num2
except TypeError as e:
    print(e)
except KeyboardInterrupt as e:#trata todos os erros de interrupcao forcada
    print("erro teclado{}".format(e))
except Exception as e:#trata todos os erros sem especificacao
    print("erro {}".format(e))