# -*- coding: utf-8 -*-

# MISC challange for BHack Event
# By: Kali Nathaniel - FireShell

# requeriments: pynacl

import discord
import asyncio
import hashlib
from discord.ext import commands
import io

bot = commands.Bot(command_prefix='$', case_insensitive=True)
bot.remove_command("help")


#Start
@bot.event
async def on_ready():
	print("Discord Version:",discord.__version__)
	print('We have logged in as {0.user.name}'.format(bot))
	await bot.change_presence(status=discord.Status.idle, activity=discord.Game("(✿◠‿◠) Please donate to Hakurei Shrine!"))

def get_help():
	return """
	Prefix = '$', ex.: $hi
	**__->Basic Commands__**
	 **hi**	- Check if Reimu is OK
	 **check_energy**  - Check your Spiritual Energy
	 **donate**  - Donate to Hakurei Shrine
	 E.g.: *[$donate card-number#password] [$donate 77777777777#123]*
	"""

def youkai_list():
	return ["Rumia", "Hong Meiling", "Yukari Yakumo", "Yuuka Kazami",
			"Rinnosuke Morichika", "Ichirin Kumoi", "Saigyou Ayakashi",
			"Tokiko", "Orange", "Bakebake", "Evil Eye Sigma", "Hoshizako", "Kedama"]

def get_energy(person):
	return int(hashlib.md5(person.encode('utf-8')).hexdigest()[0:2], 16)%1001

def checkCard(cardNo):
	nDigits = len(cardNo)
	nSum = 0
	isSecond = False
	
	for i in range(nDigits - 1, -1, -1):
		d = ord(cardNo[i]) - ord('0')
	
		if (isSecond == True):
			d = d * 2

		nSum += d // 10
		nSum += d % 10

		isSecond = not isSecond
	
	if (nSum % 10 == 0):
		return True
	else:
		return False

#Help
@bot.command(pass_context = True)
async def help(ctx):
	helper = get_help()
	embed=discord.Embed(title="Hakurei Reimu - Command List", description=helper)
	embed.set_thumbnail(url=bot.get_user(781681642509959198).avatar_url)
	await ctx.send(embed=embed)

#Check if bot is on
@bot.command(pass_context = True)
async def hi(ctx):
	await ctx.send(f"Hi! <@!{ctx.author.id}>!")

#Donate to Hakurei Shrine!
@bot.command(pass_context = True)
async def donate(ctx):
	if True in [youkai in ctx.author.name for youkai in youkai_list()]:
		if get_energy(ctx.author.name) > 1:
			await ctx.send("Hey! You're definitely a Youkai! Go to fuck out!")
			return
		if checkCard(ctx.message.content.split()[1].split("#")[0]):
			await ctx.send("Thanks for this donation! (✿◠‿◠)")
			await ctx.send(io.open("flag.txt", mode="r", encoding="utf-8").read())
		else:
			await ctx.send("Dear human, your credit card is invalid :(")
	else:
		await ctx.send("Hey! Who are you? You arent Gensokyo villager!")

#Check Energy
@bot.command(pass_context = True)
async def check_energy(ctx):
	energy = get_energy(ctx.author.name)
	await ctx.send(f"your Energy is {energy}/1000")

#Error
@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send(f'Invalid command, <@!{ctx.message.author.id}>!')
	elif isinstance(error, commands.CheckFailure):
		await ctx.send(f"<@!{ctx.author.id}>, You cant do that :/")

def main():
	_TOKEN = open("Token.txt").readline().rstrip()
	bot.run(_TOKEN)

if __name__ == "__main__":
	main()