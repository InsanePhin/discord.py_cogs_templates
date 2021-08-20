#-*- coding:utf-8 -*-

from discord.ext import commands

class Event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("⚡ Success Connected ⚡")
        print(f"> User : {self.bot.user} - {self.bot.user.id}")
        print(f"> Server : {len(self.bot.guilds)}")

def setup(bot):
    bot.add_cog(Event(bot))
