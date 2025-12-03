import discord
from discord.ext import commands
from  bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'Fizemos login como {bot.user}')

@bot.command()
async def oi(ctx):
    await ctx.send(f'Oi! Eu sou o {bot.user}!')

@bot.command()
async def senha(ctx):
    await ctx.send(f"Sua senha é:" + " " + gen_pass(10))

@bot.command()
async def tchau(ctx):
    await ctx.send(f"\U0001f642")

bot.run("<Seu token aqui>")
