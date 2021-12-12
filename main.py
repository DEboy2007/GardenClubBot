import discord
from discord.ext import commands, tasks
import keep_alive
import random

responses = ["You missed dum dum", "You hit lol", "You're a coward and dropped the snow because it was too cold"]

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
    new_str = ""
    for i in arg.split():
        new_str += i + "_"
    new_str = new_str[:-1]
    await ctx.send(f"https://en.wikipedia.org/wiki/{new_str}")


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
    new_str = new_str[:-1]
    await ctx.send(f"https://www.youtube.com/results?search_query={new_str}")

@client.command()
async def throw(ctx, arg):
  await ctx.send(f"{random.choice(responses)}. Snowball throwed towards {arg}")

@client.command()
async def youaregay(ctx):
    await ctx.send("NO YOU YOURE THE ONE WHOSE MOM IS UNDER LEGAL DRINKING AGE GET A LIFE GET A GIRLFREIND!")
    
keep_alive.keep_alive()

client.run(TOKEN)
