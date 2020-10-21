#!/home/dis/bin/python3
import os
import random
import discord
from discord import channel
from dotenv import load_dotenv

intents = discord.Intents.all()

load_dotenv('/home/.TOKEN')
TOKEN = os.getenv('TOKEN')

client = discord.Client(intents=intents)


@client.event
async def on_message(message):
    if message.content.lower() == 'hello':
        msg = await message.channel.send('gang gang yo')
    if message.content.lower() == 'olle':
        msg = await message.channel.send('enna olle')
    if message.content.lower() == 'blue balls':
        msg = await message.channel.send('<@493980666879410177>')
    if message.content.startswith('<@744622818721005630>'):
        msg = await message.channel.send('Olle goddess has been summoned.')
    if message.content == 'hocus pocus' and message.author.name == 'abaidisaac':
        def is_me(m):
            return m.author == client.user
        await message.channel.purge(limit=15, check=is_me)
    
    rpg = ['rpg', 'Rpg', 'RPG']
    for word in rpg:
        if message.content.count(word) > 0:
            if message.channel.name != 'rpg-2' and message.author.name != 'olle':
                await message.channel.send('otha why here rpg, play in rpg-2 channel.')
                    
    #bad_words = ["hocus pocus"]
    #for word in bad_words:
        #if message.content.count(word) > 0:
            #def is_me(m):
                #return m.author == client.user
            #deleted = await message.channel.purge(limit=100, check=is_me)


@client.event
async def on_typing(channel,user,when):
    if user.name == 'missinfinity':
        a = ['shut up shivani', 'stop typing shivani', 'why shivani']
        for a in random.sample(a,1):
            await channel.send(a)

#async def on_typing(channel,user,when):
    #for i in client.get_all_members():
        #print(i.name+'='+str(i.id))


@client.event 
async def on_message_delete(message):
    if message.author.name != 'abaidisaac' and message.author.name != 'olle':
        await message.channel.send(message.author.name+" deleted the message "+message.content) 


@client.event 
async def on_voice_state_update(member, before, after):
    ipl = client.get_channel(761581276615671829)
    anime = client.get_channel(761696715165401118)
    if after.self_stream == True:
        if after.channel.name == 'ipl':
           await ipl.send(member.name+" is streaming in IPL voice chat.")
        elif after.channel.name == 'anime':
            await anime.send(member.name+" is streaming in anime voice chat.")

client.run(TOKEN)