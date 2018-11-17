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
import youtube_dl








bot=commands.Bot(command_prefix='h!')

@bot.event
async def on_ready():
	print('The bot is ready!')
	print(bot.user.name)
	print(bot.user.id)
	print('----------------------------')

@client.command(pass_context=True)
async def dev():
    embed = discord.Embed(
        title = "Bot Developer",
        description = "@Kazuto Kirigaya#8757 is the owner...... also DM him about any command suggestions or if any extra help is needed",
      
	colour = discord.Colour.blue()	
	    
) 

   await bot.say(embed=embed)
		 
@client.command(pass_context=True)
async def CoO():
    embed = discord.Embed(
        title = "Co-Owner",
        description = """
        Co-Owner of this server is Mrs.Nela
        """,
        
        color = discord.Color.dark_blue()
       
)
   
    await bot.say(embed=embed)
	
		
@bot.command()
async def SCP():
	await bot.say('well want info on the foundation i think the link is Https://SCP-wiki.com i will update this command if needed')
	
@bot.command()
async def suggestion():
	await bot.say('ok DM my owner Kazuto Kirigaya#8757 and say i have a suggestion and i he will get to you when he can')
	
@bot.command()
async def extra():
	await bot.say('same with the h!suggestion command DM my owner Kazuto Kirigaya#8757 and say i need help and he will get to you when he can')

bot.run(os.getenv('BOT_TOKEN'))


