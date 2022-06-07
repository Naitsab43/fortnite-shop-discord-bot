import os
from typing import Tuple
import discord
from discord.ext import commands

class FortniteBot:

  client = None
  
  def __init__(self, command_prefix):
    self.client = commands.Bot(command_prefix=command_prefix)

  def create_embed(self, title, color, description, filepath, image_name) -> Tuple[discord.Embed, discord.File]:

    embed = discord.Embed(title=title, colour=color)

    file = discord.File(filepath)
    embed.set_image(url=f"attachment://{image_name}")

    embed.description = description


    return embed, file

  def run(self, BOT_TOKEN):
    self.client.run(BOT_TOKEN)
    