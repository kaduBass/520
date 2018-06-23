#!  /usr/bin/python3
# introducao pyhton

msg=int(input("informe um numero"))
msg1=int(input("informe outro numero"))
media = round(msg+msg1/2) 
if media >= 23:
    se="acima"
    
elif media == 23:
    se="igual"
     
else:
    se="abaixo"
    

print("a media é {} ".format(se))
