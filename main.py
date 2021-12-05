import discord
from discord.ext import commands, tasks

with open("token.txt") as token:
    TOKEN = token.read()

help_message = """Use prefix $
*$info* - Displays this message
*$hello* - Say hello back
*$amogus* - Say sus back
*$rickroll - Rickrolls you!
*$wiki **topic*** - links wikipedia page about topic specified
*$code* - Links source code"""

client = commands.Bot(command_prefix="$")


@client.event
async def on_ready():
    print("Bot Logged In")


@client.command()
async def info(ctx):
    await ctx.send(help_message)


@client.command()
async def hello(ctx):
    await ctx.send("Hello!")


@client.command()
async def amogus(ctx):
    await ctx.send("sus")


@client.command()
async def wiki(ctx, arg):
    await ctx.send(f"https://en.wikipedia.org/wiki/{arg}")


@client.command()
async def code(ctx):
    await ctx.send("https://github.com/DEboy2007/GardenClubBot")


@client.command()
async def rickroll(ctx):
    await ctx.send(
        "https://tenor.com/view/rick-roll-rick-ashley-never-gonna-give-you-up-gif-22113173"
    )


client.run(TOKEN)
