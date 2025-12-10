import discord
from discord.ext import commands
from  bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)
            
@bot.event
async def on_ready():
    print(f'Fizemos login como {bot.user}')

@bot.event
async def on_message_edit(before, after):
    msg = '**' + str(before.author) + '** editou a mensagem:\n' + before.content + ' -> ' + after.content
    await before.channel.send(msg)

@bot.command()
async def gif(ctx):
    await ctx.send(f'https://tenor.com/view/ericamyerikaemma-gif-10240140213518560872')

@bot.command()
async def emoji(ctx):
    await ctx.send(f':sob:')

@bot.command()
async def membros(ctx):
    total = ctx.guild.member_count
    await ctx.send(str(total))

@bot.command()
async def userid(ctx):
    await ctx.send(str(ctx.author.id))

@bot.command()
async def senha(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def emojiid(ctx, emoji: str):
    if emoji.startswith("<") and emoji.endswith(">"):
        emoji_id = emoji.split(":")[-1].replace(">", "")
        await ctx.send(emoji_id)

@bot.command()
async def formatobio(ctx):
    format = "<:(emoji_name):(emoji_id)>"
    await ctx.send(format)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def nuke(ctx):
    await ctx.message.delete()
    await ctx.channel.purge(limit=None)

@bot.command()
async def ajuda(ctx):
    mensagem = ''
    for cmd in bot.commands:
        mensagem += f"> .{cmd.name}\n"
    await ctx.send(mensagem)

bot.run("(Token)")
