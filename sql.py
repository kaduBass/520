#!  /usr/bin/python3
import psycopg2

try:
   con = psycopg2.connect("host=127.0.0.1\
   dbname=projeto user=admin password=4linux") 
   cur = con.cursor()
   entrada = "UPDATE usuarios SET nome='ana lucia' WHERE id=2"
   cur.execute(entrada)
   #entrada = "INSERT INTO usuarios (nome,idade) values ('ricardo',212)"
   #entrada = "SELECT nome FROM usuarios"
   
   
   #res=cur.fetchone()
   res=cur.fetchone()
   con.commit()
   cur.close()
   cur.close()
except Exception as erro:
    con.rollback()#de errado volta pro estado inicial
    con.rollback()
    print("erro {}".format(erro))
  