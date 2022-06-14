# imports
import discord
from discord.ext import commands, tasks

#set the client
client = commands.Bot(command_prefix="+")

@client.command(name="kick", help="kicks a user) #client command
async def kick(ctx, member = discord.member, *, reason = None):

  if reason == None:
    reason = F"{ctx.author} gave no reason given"

  try:
    member.kick(reason = reason)
    await ctx.send(F"Sucsesfully kicked {member}")
  except:
    await ctx.send("There was a Problem")

client.run("your token here")
