# imports
import discord
from discord.ext import commands, tasks

#set the client
client = commands.Bot(command_prefix="T!")

@client.command(description="kicks a user with specific reason (only admins)")
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.User = None, reason=None):
    try:
        if (reason == None):
            embeds = discord.Embed(
            title=f"You have to give a reason to kick {member}!",
            color=discord.Color.blue())

            await ctx.reply(embed=embeds)
            return
        if (member == ctx.message.author or member == None):
            await ctx.channel.send("""You cannot kick yourself!""")

        embed = discord.Embed(
            title="Kicked!",
            description=f"You have been kicked from **{ctx.guild.name}** for   **{reason}**! \n \n \n Support Server: https://discord.gg/BTBrTPRa6X",
            color=discord.Color.blue())
        await member.send(embed=embed)
        await ctx.guild.kick(member, reason=reason)
        print(member)
        print(reason)
        await ctx.channel.send(f"{member} was kicked!")
    except:
        embed2 = discord.Embed(
            title=f"{member} is kicked!",
            color=discord.Color.blue())
        await ctx.channel.send(embed=embed2)
    
client.run("your token here")
