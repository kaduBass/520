#!  /usr/bin/python3
# introducao pyhton
import glob #retorna uma lista glob.glob dos arquivos
try:
    arquivo=input("informe nome do arquivo")
    
    if arquivo=="privado":
        #nao tem direito a acesso a este arquivo
        raise FileNotFoundError
    else:
        print(len(glob.glob("*.olp",recursive=True)))
       
           

            
except FileNotFoundError as erro:
    print("nao econtrado o arquivo")








