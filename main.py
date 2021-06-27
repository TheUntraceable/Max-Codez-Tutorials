import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix = '?', intents=discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)

client.run('ODU1NDc5NDA0Njc1MzM0MTg0.YMzFSA.dV1EU9wkYrP7IH0GVjpHOZ_vQf0')
