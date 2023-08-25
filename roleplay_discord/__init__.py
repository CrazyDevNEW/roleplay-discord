import discord
from datetime import datetime
import os
from discord.ext import commands
from discord.ui import Button, View

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
async def ping(interaction):
    await interaction.response.send_message("Pong!")

class ButtonsMenu(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Join", style=discord.ButtonStyle.green)
    async def button1(self, interaction:discord.Interaction, button:discord.ui.Button):
        await interaction.response.send_message("Ещё не работает!")

    @discord.ui.button(label="About", style=discord.ButtonStyle.blurple)
    async def button2(self, interaction:discord.Interaction, button:discord.ui.Button):
        await interaction.response.send_message("Тем более не работает!")

    @discord.ui.button(label="Documentation", style=discord.ButtonStyle.grey)
    async def button3(self, interaction:discord.Interaction, button:discord.ui.Button):
        await interaction.response.send_message("...")

@tree.command(name="join")
async def join(interaction):
    view=ButtonsMenu()
    embed=discord.Embed(title="Стартовое меню", description=f"Это стартовое окно, где вы можете выбрать действия перед чем начать игру.", color=0xAEF359)
    embed.set_footer(text='Приятной игры')
    await interaction.response.send_message(embed=embed,view=view)

if __name__ == "__main__":
    client.run(config.discordApiToken)
