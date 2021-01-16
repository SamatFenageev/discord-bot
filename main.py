import discord
from discord.ext import commands
from random import randint, choice

client = commands.Bot(command_prefix = '!')

gays = ['артём гей', 'артем гей', 'олег гей']
straight = ['артём натурал','артем натурал']
@client.event

async def on_ready():
	print('bot connected')

@client.command(pass_context = True)

async def hello(ctx):
await ctx.send('Hop Hey!\nArtem gay (:')

@client.event

async def on_message(message):
	msg = message.content.lower()

	if msg in gays:
		await message.channel.send('Да-да, он самый!')



async def help(ctx):
	emb = discord.Embed(title = 'навигация по командам')

	emb.add_field()

#Connecting

token = open('token.txt', 'r').readlines()



client.run(token[1])
