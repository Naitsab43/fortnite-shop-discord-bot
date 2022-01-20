import discord
import os
from discord.ext import commands
from datetime import date, datetime
from concat_images import create_image_store

TOKEN = "*token*"

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
  print("El bot esta activo")


# Muestra los comandos
@client.command()
async def shop(ctx):

  await create_image_store();

  day = datetime.now()
  month = day.strftime("%B")

  day = day.strftime("%A")

  if day == "Monday":
    day = "Lunes"
  elif day == "Tuesday":
    day = "Martes"
  elif day == "Wednesday":
    day = "Miércoles"
  elif day == "Thursday":
    day = "Jueves"
  elif day == "Friday":
    day = "Viernes"
  elif day == "Saturday":
    day = "Sábado"
  elif day == "Sunday":
    day = "Domingo"

  if month == "January":
    month = "Enero"
  elif month == "February":
    month = "Febrero"
  elif month == "March":
    month = "Marzo"
  elif month == "April":
    month = "Abril"
  elif month == "May":
    month = "Mayo"
  elif month == "June":
    month = "Junio"
  elif month == "July":
    month = "Julio"
  elif month == "August":
    month = "Agosto"
  elif month == "September":
    month = "Septiembre"
  elif month == "October":
    month = "Octubre"
  elif month == "November":
    month = "Noviembre"
  elif month == "December":
    month = "Diciembre"
  
  date_today = date.today()
  day_number = date_today.day
  year = date_today.year


  embed = discord.Embed(title= f"💰 Tienda de fortnite - {day} {day_number} de {month} del {year}", colour=discord.Colour.blue())

  filee = discord.File("src/images/shop/shop.png")

  embed.description = "No me pagan lo suficiente, vayanse a la chucha"

  embed.set_image(url="attachment://shop.png")
  
  await ctx.send(file= filee, embed=embed)


if __name__ == "__main__":
  client.run(TOKEN)
