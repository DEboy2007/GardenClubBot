import discord
from discord.ext import commands, tasks
import keep_alive

with open("token.txt") as token:
    TOKEN = token.read()

with open("help.txt") as help:
    help_message = help.read()

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


@client.command()
async def say(ctx, arg):
    await ctx.send(arg)

@client.command()
async def yt(ctx, arg):
  new_str = ""
  for i in arg.split():
    new_str += i + "+"
  await ctx.send(f"https://www.youtube.com/results?search_query={new_str}")

keep_alive.keep_alive()

client.run(TOKEN)
