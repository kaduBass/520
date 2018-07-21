#!  /usr/bin/python3
import asyncio

@asyncio.coroutine
def empacotar_bala():
    print("Empacotando balas...")

  


@asyncio.coroutine
def atender_balcao():
    print("Explicitamente verificando se tem cliente no balcão...")

   


ioloop = asyncio.get_event_loop()  # Event Loop

tasks = [ioloop.create_task(empacotar_bala()),
         ioloop.create_task(atender_balcao())]

wait_tasks = asyncio.wait(tasks)

ioloop.run_until_complete(wait_tasks)

ioloop.close()