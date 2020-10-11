import discord
import os
import traceback
from discord import member
from discord.ext import commands

client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_member_join(member):
    if member.guild.id == (750342034124046397):
        channel_sent = client.get_channel(750342034572967969)
        if member.id == (723814754572959764):
            user = discord.utils.get(member.guild.members, id=723814754572959764)
            await user.kick()

client.run(token)
