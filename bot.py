import discord 
from random import randint
import json



class MyClient(discord.Client):
    
  
    async def on_ready(self):
        print(f'Logged on as { self.user}!')
         
        
        

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        comado = str(message.content)
        comado.split()
        if comado == '/help':
            await message.channel.send(f'{message.author.name} ex: 4d6  redona ')
        if ',' in comado:
            try:
                p = comado.find(',')
                comado1= comado[0:p] 
                mod = int(comado[p+1:])
                if comado1== '/rolar': 
                    dado = randint(1,20)
                    dadom = dado + mod
                    await message.channel.send(f'{message.author.name}  seu dado é {dado} mais seu modificado é de {mod}-> :{dadom}')
                else:
                    pass
            except:
                pass
        elif comado == '/rolar':
            dado = randint(1,20)
            await message.channel.send(f"{message.author.name} -> : {dado}")
        

        message1 = str(message.content)
        message1 = message1.lower()
        d1 = []
        if message1: 
            try:
                
                d=message1.find('d') 
                qua= int(message1[0:d])
                fase =int( message1[d+1:]) 
                for nq in range(1,qua+1):
                    nq = randint(1,fase)
                    d1.append(nq)
                await message.channel.send(f'{message.author.name}->  {d1}')
            except:
    
                pass
        
                # await message.channel.send(f'{message.author.name} me')
    def info(self):
        if self.r == None:
            pass
        else:
            return str(self)
try:
    arquivo = open('token.json', 'r',encoding='utf-8')
    dado = json.load(arquivo)
    chave = dado['token']
    client = MyClient()
    client.run(chave)

except:
   print(1)  

# client = MyClient   
# client.run('')

    




