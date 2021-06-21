#-*- coding:utf-8 -*-

import discord, asyncio, datetime, os
from discord.ext import commands

TOKEN=# YOUR TOKEN HERE
PREFIX=# BOT PREFIX HERE

bot = commands.Bot(help_command=None, command_prefix=commands.when_mentioned_or(PREFIX), intents=discord.Intents.all())

for filename in os.listdir('modules'):
    if filename.endswith('.py'):
        try:
            bot.load_extension("modules." + filename[:-3])
        except Exception as e:
            print(f'failed loaded. file : {filename} error : {e}')


@bot.command(aliases=['reload', 'rl'])
@commands.is_owner()
async def _reload_all(ctx):
    error_collection = []
    for file in os.listdir("modules"):
        if file.endswith(".py"):
            name = file[:-3]
            try:
                bot.reload_extension(f"modules.{name}")
            except Exception as e:
                error_collection.append(
                    [file, e]
                )

    if error_collection:
        output = "\n".join(
            [f"**{g[0]}**" for g in error_collection]
        
        )
        return await ctx.send(
            f"Check the {output} file"
        )

    return await ctx.message.reply(f"reloaded `{len(bot.commands)}` commands.")

@_reload_all.error
async def reloadall_handler(ctx, error):
    pass

bot.run(TOKEN)
