# bot.py

import discord

from settings import settings

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


client.run(settings["discord_token"])
