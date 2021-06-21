#-*- coding:utf-8 -*-

import discord, asyncio, requests, os
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



def setup(bot):
    bot.add_cog(Admin(bot))