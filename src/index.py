import os
import discord
from config import BOT_TOKEN
from fortnite_bot import FortniteBot
from fortnite_image import FortniteImage
from utils import get_actual_date_formatted

fortnite_bot = FortniteBot(command_prefix="!")
fortnite_image = FortniteImage()

@fortnite_bot.client.event
async def on_ready():
  print("El bot esta activo")

@fortnite_bot.client.command()
async def shop(ctx):

  is_one_image = fortnite_image.create_image_store()

  date = get_actual_date_formatted()

  if(is_one_image):
    embed, file = fortnite_bot.create_embed(
      title=f"💰 Tienda de fortnite - {date['day']} {date['day_number']} de {date['month']} del {date['year']}", 
      color=discord.Colour.blue(), 
      description="Fortnite shop",
      filepath="src/assets/images/shop/shop.png",
      image_name="shop.png"
    )
    await ctx.send(file=file, embed=embed)
    os.remove("src/assets/images/shop/shop.png")
    return
  
  embed, file = fortnite_bot.create_embed(
    title=f"💰 Tienda de fortnite - {date['day']} {date['day_number']} de {date['month']} del {date['year']}", 
    color=discord.Colour.blue(), 
    description="Fortnite shop",
    filepath="src/assets/images/shop/shop1.png",
    image_name="shop1.png"
  )

  await ctx.send(file=file, embed=embed)

  embed, file = fortnite_bot.create_embed(
    title="", 
    color=discord.Colour.blue(), 
    description="",
    filepath="src/assets/images/shop/shop2.png",
    image_name="shop2.png"
  )

  await ctx.send(file=file, embed=embed)

  os.remove("src/assets/images/shop/shop1.png")
  os.remove("src/assets/images/shop/shop2.png")
  
if __name__ == "__main__":
  fortnite_bot.run(BOT_TOKEN)
