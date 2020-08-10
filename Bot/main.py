import discord
import os, random, asyncio, time
from discord.ext import commands

token = 'NzQyNDEzMjc3ODMyODA2NDQw.XzFwPg.-OlfeEap75uL--CSMMn0TIYC6is'

bot = commands.Bot(command_prefix="!", activity=discord.Activity(name="Whale | !help", type=1))

@bot.event
async def on_ready():
    print("Logged in as: "+ bot.user.name)

class Jaram(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx):
        """Show bot's internet connection"""
        await ctx.send("Pong! `{0}ms`".format(round(bot.latency, 6)))

    @commands.command()
    async def admin(self, ctx):
        """자람 임원진을 소개합니다"""
        message = '```\n자람 임원진을 소개합니다.\n회장 : 유진웅.35\n부회장 : 이승훈.35\n서버관리자 : 강찬영.35\n학술부장 : 홍석민.35\n홍보부장 : 박예빈.35\n섭외부장 : 전상민.35\n회계 : 임종협.35\n```'
        await ctx.send(message) 

class Whale(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def whale(self, ctx):
        """Show random pictures of whale emoticon"""
        pick = random.randrange(1, 30)
        await ctx.send(file=discord.File('image/'+str(pick)+'.png'))

#bot Catergory
bot.add_cog(Whale(bot))
bot.add_cog(Jaram(bot))

bot.run(token)