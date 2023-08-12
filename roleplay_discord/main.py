import discord
import os
import logging
from datetime import datetime
import config

intents = discord.Intents.default()
client = discord.Client(intents=intents)

class WorldObject:
    def __init__(self, *args, **kwargs):
       self.world = kwargs.get("world")
       self._posX = kwargs.get("posX")
       self._posY = kwargs.get("posY")

class MoveObject:
    def moveObject(self, obj):
        pass

class Wall(WorldObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.callisia = True
        self.destroy = 50
        self.touch_damage = False
        self.locate_damage = 500

class Ground(WorldObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.callisia = False
        self.destroy = 50
        self.touch_damage = False
        self.locate_damage = False

class World:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.size_x = kwargs.get("size_x")
        self.size_y = kwargs.get("size_y")
        self.map = kwargs.get("map")
    
class Player(WorldObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.member = kwargs.get("member")
    

@client.event
async def on_ready() -> None:
    print("Bot ready!")

if __name__ == "__main__":
    now = datetime.now().strftime(config.time_format)
    try:
        handler = logging.FileHandler(filename=f'logs/{now}.log', encoding='utf-8', mode='w')
    except FileNotFoundError:
        os.mkdir("logs/")
        handler = logging.FileHandler(filename=f'logs/{now}.log', encoding='utf-8', mode='w')
    client.run(config.discordApiToken, log_handler=handler, log_level=config.log_level)
