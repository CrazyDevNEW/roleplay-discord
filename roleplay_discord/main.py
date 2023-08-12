import discord
import logging
from discord import app_commands
import config

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready() -> None:
    print("Bot ready!")


handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
client.run(config.discordApiToken, log_handler=handler, log_level=config.log_level)
