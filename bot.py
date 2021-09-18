import discord
import json
import requests
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from settings import cfg

bot = commands.Bot(command_prefix = cfg['prefix'])

@bot.command()
@has_permissions(kick_members = True)
async def news(ctx, *, text):
    embed = discord.Embed(
    	title = 'Новости',
    	color = 0xff9900,
    	description = text
    )
    await ctx.message.delete()
    await ctx.send(embed = embed)

@news.error
async def news_error(error, ctx):
	if isinstance(error, MissingPermissions):
		await bot.send_message(ctx.message.channel, 'У вас нет прав!')
bot.run(cfg['token'])
