#!/home/dis/bin/python3
import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = 'NzY2NTU2NjI3MTk2MTgyNTI5.X4lFfQ.b5kSDZt1oRnjCsbU7WvnB68fo1s'
GUILD = 'abaid'
client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('hello'):
        msg = await message.channel.send('gang gang yo')

@client.event
async def on_typing(channel,user,when):
    print(user)

client.run(TOKEN)