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







client = commands.Bot(command_prefix = 'h!')


players = {}

status = ['>help for commands', 'With code', "Stabbing Mrs.Nela","With developer Mrs.Nela"]

players = {}



@client.event
async def on_ready():
    print("The bot is online and connected with Discord!")

@client.command(pass_context = True)
async def dev():
    embed = discord.Embed(
        title = "Bot Developer:",
        description = "@Kazuto Kirigaya#8757 is the owner...... also DM him about any command suggestions or if any extra help is needed",
    color = discord.Colour.blue()
)
    await client.say(embed=embed)

@client.command(pass_context = True)
async def CoO():
    embed = discord.Embed(
       title = "Co-Owner",
       description = "Co-Owner is @Mrs.Nela#8429!",
    color = discord.Colour.dark_blue()
)
    await client.say(embed=embed)

@client.command()
async def SCP():
	await bot.say("well want info on the foundation i think the link is Https://SCP-wiki.com i will update this command if needed")
	
@client.command()
async def suggestion():
	await bot.say("ok DM my owner Kazuto Kirigaya#8757 and say i have a suggestion and i he will get to you when he can")
	
@client.command()
async def extra():
	await bot.say("same with the h!suggestion command DM my owner Kazuto Kirigaya#8757 and say i need help and he will get to you when he can")
	
client.run(os.getenv("BOT_TOKEN"))


