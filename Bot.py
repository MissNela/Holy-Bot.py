import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import platform
import colorsys
import random
import os
import time
from discord.voice_client import VoiceClient
from discord import Game, Embed, Color, Status, ChannelType









bot=commands.Bot(command_prefix='h!')

@client.event
async def on_ready():
	print('The bot is ready!')
	print(bot.user.name)
	print(bot.user.id)
	print('----------------------------')

@client.command()
async def dev():
    

         
   await client.say("@Kazuto Kirigaya#8757 is the owner...... also DM him about any command suggestions or if any extra help is needed")
		 
@client.command()
async def CoO():
    
    await client.say("Co-Owner of server is Mrs.Nela!")
	
		
@client.command()
async def SCP():
	await client.say('well want info on the foundation i think the link is Https://SCP-wiki.com i will update this command if needed')
	
@client.command()
async def suggestion():
	await client.say('ok DM my owner Kazuto Kirigaya#8757 and say i have a suggestion and i he will get to you when he can')
	
@client.command()
async def extra():
	await client.say('same with the h!suggestion command DM my owner Kazuto Kirigaya#8757 and say i need help and he will get to you when he can')

bot.run(os.getenv('BOT_TOKEN'))


