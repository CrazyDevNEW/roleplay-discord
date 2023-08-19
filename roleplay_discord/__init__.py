import discord
import logging
from datetime import datetime
import os

import config

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

now = datetime.now().strftime(config.time_format)
logs_path = "roleplay_discord/logs/"
try:
    handler = logging.FileHandler(filename=f'{logs_path}{now}.log', encoding='utf-8', mode='w')
except FileNotFoundError:
    os.mkdir(logs_path)
    handler = logging.FileHandler(filename=f'{logs_path}{now}.log', encoding='utf-8', mode='w')

@client.event
async def on_ready() -> None:
    for command in tree.get_commands():
        tree.add_command(command)
    try:
        await tree.sync()
    except discord.app_commands.CommandAlreadyRegistered:
        pass
    print("Bot ready!")

@tree.command(name="ping", description="Request pong!")
async def ping(interection):
    await interection.response.send_message("Pong!")

if __name__ == "__main__":
    client.run(config.discordApiToken, log_handler=handler, log_level=config.log_level)
