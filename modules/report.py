#-*- coding:utf-8 -*-

import discord, asyncio, requests, os
from discord.ext import commands

class Report(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



def setup(bot):
    bot.add_cog(Report(bot))