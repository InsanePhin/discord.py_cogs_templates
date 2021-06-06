#-*- coding:utf-8 -*-

import discord, asyncio, datetime, os, config
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv(verbose=True)
bot = commands.Bot(help_command=None, command_prefix=commands.when_mentioned_or(os.getenv("prefix")), intents=discord.Intents.all())

for filename in os.listdir('modules'):
    if filename.endswith('.py'):
        try:
            bot.load_extension("modules." + filename[:-3])
        except Exception as e:
            print(f'{filename} 로드에 실패했습니다. 에러 : {e}')


@bot.command(aliases=['ㄹㄹㄷ', '리로드', 'ffe'])
@commands.is_owner()
async def reloadall(ctx):
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

    return await ctx.message.reply(f"`{len(bot.commands)}개`의 명령어를 `리로드`하였습니다.")

@reloadall.error
async def reloadall_handler(ctx, error):
    pass

bot.run(os.getenv("token"))
