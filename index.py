#-*- coding:utf-8 -*-

import discord, os, jishaku
from discord.ext import commands

TOKEN=""    # YOUR TOKEN HERE
PREFIX=""   # BOT PREFIX HERE

bot = commands.Bot(help_command=None, command_prefix=commands.when_mentioned_or(PREFIX), intents=discord.Intents.all())

bot.load_extension("Jishaku")
for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        try:
            bot.load_extension("cogs." + filename[:-3])
        except Exception as e:
            print(f'failed loaded. file : {filename} error : {e}')

bot.run(TOKEN)
