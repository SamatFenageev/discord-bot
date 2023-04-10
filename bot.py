import discord
from discord.ext import commands
from random import choice, uniform
import re
import datetime
from time import sleep

intents = discord.Intents.default()
intents.members = True


client = commands.Bot(command_prefix = '!', intents=intents)
client.remove_command('help')
#r'арт.м'
gays = [r'арт.м гей', 'олег гей']
straight = [r'арт.м натурал',
		'олег натурал']
jokes = ['Ты тут за меня придурка не держи, он же Натуральный Гей',
 			'фига ты клоун,иди в цирк, не позорься :clown:',
			'а это не он там на коленях перед каким-то мужиком без штанов?)',
			'Ага, конечно, а меня создал человек с мозгами, как же :lying_face:',
			'возможно, но  всё же его рот стоит своих денег :money_mouth:',
			'ты про того, что гей?',
			'хорошо, хорошо, только убери его от моего 4лЕна, пожалуйста :sob:']

agreements = ['Да-да, он самый!', 'А вы сомневаетесь?..', 'Полностью с вами солидарен.',
			'Согласен. 🗿', 'Определённо!', 'Ни доли сомнений!', 'Нет, блин, натурал 🗿']

owner = ['Вы про моего хозяина?','Да-да, мой хозяин таков.','Это мой хозяин.', 'Хозяин?']

members = {'Hyxai Bebry #3722':'Елисей','Monstrik #3943':'Олег','REGET #7509':'Костя','sasa# 9969':'Саня',
			'trap zone #8124':'Егор','катет #8622':'Диляра','монашка #8450':'Динара','♣𝓘𝓽𝔃𝓛𝓾𝓬𝓴𝔂♣ #5632':'Карина З.',
			'[1]Matvei Zhopoevskie #7082':'Матвей','KurtCocaine. #9953':'Эмиль','baguette #9160':'Артём',
			'Gaymer #0107':'Самат', 'حب الكلاب#9803': 'Арина'}

names = list(members.values())



@client.event

async def on_ready():
	print('bot connected')
	await client.change_presence( activity = discord.Game('Gay Porn'))
	for guild in client.guilds:
		for member in guild.members:
			print(member)
	
#количество упомянаний геев
@client.command(pass_context = True)

async def counter(ctx):
	counter_file = open('counter.txt','r')
	gay_counter = int(counter_file.readline())
	counter_file.close()
	ending = '' if gay_counter%10 <= 1 or 5<=gay_counter%10<=9 or gay_counter//10 == 1 else 'а' 
	await ctx.send(f'Вы упомянули Геев {gay_counter} раз{ending}')

#hello comand
@client.command(pass_context = True)

async def hello(ctx):
	await ctx.send('Hop Hey!\nArtem gay (:')

#clear command
@client.command(pass_context = True)

async def clear(ctx, amount = 10000):
	await ctx.channel.purge(limit = amount)

@client.command(pass_context = True)

async def test(ctx):
	
	if ctx.message.author.name == 'baguette' or ctx.message.author.name == 'Monstrik':
		percent = round(uniform(1000,10000), 2)
		await ctx.send(f'You are {percent}% 🏳️‍🌈Gay🏳️‍🌈 at the moment, glad to see you, True Dungeon Master! 🤝🍆🤝')

	#if ctx.message.author.name == 'Gaymer':
		#await ctx.send('You are 100% Sraight')

	else:
		percent = round(uniform(0,100), 2)
		if percent >=80:
			await ctx.send(f'You are {percent}% 🏳️‍🌈Gay🏳️‍🌈 at the moment, glad to see you, True Dungeon Master! 🤝🍆🤝')

		elif percent >= 50:
			await ctx.send(f'You are {percent}% 🏳️‍🌈Gay🏳️‍🌈 at the moment, keep it up, Buddy! 👋🍑')

		elif percent>=30:
			await ctx.send(f'You are only {percent}% 🏳️‍🌈Gay🏳️‍🌈 at the moment, feel sorry for You, Buddy, Here, enjoy drinking my Cum Collection 🥛 and cheer up')

		else:
			await ctx.send(f'You are only {percent}% 🏳️‍🌈Gay🏳️‍🌈 at the moment, no Nomo, let\'s just have True Men\'s $ex 🍆💦')

#pidor command
@client.command(pass_context = True)

async def pidor(ctx):
	file = open('pidorDate.txt', 'r')
	last_time = datetime.datetime.strptime(file.readline(),"%d/%m/%y %H:%M")
	file.close()

	now = datetime.datetime.today()
	with codecs.open('pidor.txt', "r",decoding='utf-16', errors='ignore') as file:
		tot_samiy = file.readline()
		if (now - last_time).days:

			tot_samiy = choice(names)
			await ctx.send(f'Инициализирую поиск пидора...')
			sleep(3)
			await ctx.send(f'Итак, пидором дня является:')
			sleep(3)
			await ctx.send(f'🏳️‍🌈 {tot_samiy} 🏳️‍🌈, 🎊🎉 поздравляем счастливчика! 🎉🎊 🥳')

			file = open('pidorDate.txt', 'w')
			file.write(datetime.datetime.strftime(datetime.datetime.now(),"%d/%m/%y %H:%M"))
			file.close()
			with codecs.open('pidor.txt', "w",encoding='utf-16', errors='ignore') as file:
				file.write(tot_samiy)
		else:

			await ctx.send(f'😔Пидор сегодняшнего дня уже выбран, им является 🏳️‍🌈 {tot_samiy} 🏳️‍🌈 \n приходите завтра, чтобы попытаться обойти его')
		

#rat command
@client.command(pass_context = True)

async def rat(ctx):
	file = open('ratDate.txt', 'r')
	last_time = datetime.datetime.strptime(file.readline(),"%d/%m/%y %H:%M")
	file.close()

	now = datetime.datetime.today()

	with codecs.open('rat.txt', "r",decoding='utf-16', errors='ignore') as file:
		tot_samiy = file.readline()
		

		if (now - last_time).days:

			tot_samiy = choice(names)
			await ctx.send(f'Среди нас затаилась крыса 🐀')
			sleep(3)
			await ctx.send(f'Вычисляю эту падлу по IP 🧀...')
			sleep(3)
			await ctx.send(f'Опа! Нашёл его, когда тот пытался зайти на порнхаб в поисках НЕгейского порно❌🏳️‍🌈')
			sleep(5)
			await ctx.send(f'Вот этот, Тьфу 💦, натурал, 🐀 {tot_samiy} 🐀')

			file = open('ratDate.txt', 'w')
			file.write(datetime.datetime.strftime(datetime.datetime.now(),"%d/%m/%y %H:%M"))
			file.close()	
			with codecs.open('rat.txt', "w",encoding='utf-16', errors='ignore') as file:
						file.write(tot_samiy)
		else:

			await ctx.send(f'😔Я уже поймал одну крысу сегодня\n Вот она 👉 🐀 {tot_samiy} 🐀\n Mеня от этих натуралов уже тошнит🤢\n Можно я отдохну от них, Сэмпай...🥺')

		
@client.command( pass_context = True)
@commands.has_permissions(administrator = True)

async def help(ctx):
	emb = discord.Embed( title = 'Доступные боту команды')
	emb.add_field( name = '!clear', value = 'Очистка чата')
	emb.add_field( name = '!rat', value = 'Крыса дня')
	emb.add_field( name = '!pidor', value = 'Пидор дня')
	emb.add_field( name = '!counter', value = 'Количество упоминаний геев')
	emb.add_field( name = '!test', value = 'Твой текущий  Gayness Level')
	emb.add_field( name = '!hello', value = 'Хрень какая-то, как и сам бот в общем-то, но почему бы и нет')

	await ctx.send( embed = emb)
@client.event

async def on_message(message):
	global gay_counter
	await client.process_commands(message)
	msg = message.content.lower()
	if straight[1] in msg or re.search(straight[0], msg):#					FIX HERE	FIX HERE	FIX HERE	FIX HERE	FIX HERE	FIX HERE	FIX HERE
		string = ''
		for i in range(choice([8,14])):
			string += choice(['a','A','x','X','П','п','В','в'])
			out = [f'{string}, ' + word for word in jokes]
		await message.channel.send(choice(out))

	if 'гей' in msg or 'лох' in msg or re.search(r'пид(арас)*(рила)*(ор)*(орас)*', msg) or 'лох' in msg:
		if re.search(r'арт.м', msg) or re.search(r'.ле.', msg):
			await message.channel.send(choice(agreements))
			counter_file = open('counter.txt','r')
			gay_counter = int(counter_file.readline())
			counter_file.close()

			gay_counter += len(re.findall(r'арт.м', msg)) + msg.count('олег')
			counter_file = open('counter.txt','w')
			counter_file.write(str(gay_counter))
			counter_file.close()
		if 'самат' in msg:
			#FIX HERE	FIX HERE	FIX HERE	FIX HERE	FIX HERE	FIX HERE	FIX HERE
			who_is = choice(['Артём', 'Олег'])
			await message.channel.send(f'Вы наверное имели ввиду {who_is}.')
		
	if re.search(r'пр.гра(м)*ист', msg):
		await message.channel.send(choice(owner))



	
#Connecting

token = open('token.txt', 'r').readlines()

client.run(token[1])

