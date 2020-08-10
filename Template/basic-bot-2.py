import asyncio
import discord

from discord.ext import commands

class BasicBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello World")


bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"),
                   description='Simple bot example')

@bot.event
async def on_ready():
    print('Logged in as {0} ({0.id})'.format(bot.user))
    print('------')

bot.add_cog(BasicBot(bot))
bot.run('token')