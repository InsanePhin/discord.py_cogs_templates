#-*- coding:utf-8 -*-

import discord, asyncio, requests, os
from discord.ext import commands

class Event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(status=discord.Status.dnd ,activity=discord.Activity(type=discord.ActivityType.playing, name=f"나락으로 질주"))
        
        print(f"⚡ Success Connected ⚡")
        print(f"// INFORMATION //")
        print(f"> User : {self.bot.user} - {self.bot.user.id}")
        print(f"> Server : {len(self.bot.guilds)}")
        

def setup(bot):
    bot.add_cog(Event(bot))