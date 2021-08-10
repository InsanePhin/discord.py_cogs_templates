#-*- coding:utf-8 -*-

from discord.ext import commands

class Command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Command(bot))
