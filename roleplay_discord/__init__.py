import discord
from datetime import datetime
import os

import config

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

#logs_path = "roleplay_discord/logs/"
#logger = logging.getLogger("discord")
#logger.setLevel("DEBUG")
#logging.getLogger("discord.http").setLevel()

@client.event
async def on_ready() -> None:
    try:
        await tree.sync()
    except discord.HTTPException:
        pass

@tree.command(name="ping", description="Request pong!")
async def ping(interection):
    await interection.response.send_message("Pong!")

if __name__ == "__main__":
    client.run(config.discordApiToken)
