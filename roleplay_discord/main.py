import discord
import logging
from datetime import datetime
from discord import app_commands
import config

intents = discord.Intents.default()
client = discord.Client(intents=intents)

class World:
    size_x = 30
    size_y = 30

class Player:
    def __init__(self, *args, **kwargs) -> None:
        self.firstname = kwargs.get("firstname")
        self.lastname = kwargs.get("lastname")


@client.event
async def on_ready() -> None:
    print("Bot ready!")

if __name__ == "__main__":
    now = datetime.now().strftime(config.time_format)
    handler = logging.FileHandler(filename=f'{now}.log', encoding='utf-8', mode='w')
    client.run(config.discordApiToken, log_handler=handler, log_level=config.log_level)
