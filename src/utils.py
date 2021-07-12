import cv2
from PIL import Image, ImageDraw, ImageFont
import io
import os
import requests

def image_to_byte(image:Image):

  imgByteArr = io.BytesIO()
  image.save(imgByteArr, format=image.format)
  imgByteArr = imgByteArr.getvalue()

  return imgByteArr

def create_empty_image(concat, concat2, concat3, concat4, concat5):
  # Agrega imagenes negras para cuando un arreglo tenga una imagen de menos
  # Restando con la cantidd de shape del arreglo uno con el que tenga menos
  
  if concat.shape != concat2.shape:
    
    list_img_empty = []

    numbers = concat.shape[1] - concat5.shape[1]
    cant_empty = int(numbers / 512)

    for i in range(0, cant_empty):
      empty_img = cv2.imread(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\Empty.png")
      empty_img = cv2.resize(empty_img, (512, 660))
      concat2 = cv2.hconcat([concat2, empty_img])


  if concat.shape != concat3.shape:

    list_img_empty = []

    numbers = concat.shape[1] - concat5.shape[1]
    cant_empty = int(numbers / 512)

    for i in range(0, cant_empty):
      empty_img = cv2.imread(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\Empty.png")
      empty_img = cv2.resize(empty_img, (512, 660))
      concat3 = cv2.hconcat([concat3, empty_img])

  if concat.shape != concat4.shape:

    list_img_empty = []

    numbers = concat.shape[1] - concat5.shape[1]
    cant_empty = int(numbers / 512)

    for i in range(0, cant_empty):
      empty_img = cv2.imread(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\Empty.png")
      empty_img = cv2.resize(empty_img, (512, 660))
      concat4 = cv2.hconcat([concat4, empty_img])

  print(concat.shape)
  print(concat5.shape)

  if concat.shape != concat5.shape:

    list_img_empty = []

    numbers = concat.shape[1] - concat5.shape[1]
    cant_empty = int(numbers / 512)

    for i in range(0, cant_empty):
      empty_img = cv2.imread(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\Empty.png")
      empty_img = cv2.resize(empty_img, (512, 660))
      concat5 = cv2.hconcat([concat5, empty_img])


  return concat, concat2, concat3, concat4, concat5

def create_final_image(images_raw, images_names, images_rarity, images_prices, images_series, images_news):

  inc_rarity = 0
  inc_names = 0
  inc_price = 0

  for image in images_raw: 

    try: 

      imagen_get = requests.get(image)

      open(f"{os.path.dirname(os.path.abspath(__file__))}/images/objects/{images_names[inc_names]}.png", "wb").write(imagen_get.content)

      if images_rarity[inc_rarity] == "common" and images_series[inc_names] == None:
        
        over = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\objects\\{images_names[inc_names]}.png").convert("RGBA")

        if over.size == (1024, 1024): 

          font_money = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 84)

          font_name = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 90)

          back = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\CommonXL.png").convert("RGBA")

          background = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\backgroundXL.png")

          if images_news[inc_names]:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottomXL-new.png").convert("RGBA")
          else:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottomXL.png").convert("RGBA")
          

          draw = ImageDraw.Draw(bottom)
          w, h = draw.textsize(str(images_names[inc_names]), font=font_name)
          draw.text((480, 170), str(images_prices[inc_names]), font=font_money, fill="white")
          draw.text(((1024-w)/2, 40), images_names[inc_names], font=font_name, fill="white")

          back.paste(over, (0,0), over)

          background.paste(back, (0,0), back)

          background.paste(bottom, (0,1024), bottom)

          final = image_to_byte(background)

        else:

          font_money = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 46)

          font_name = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 48)

          back = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\Common.png").convert("RGBA")

          background = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\background.png")

          if images_news[inc_names]:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottom-new.png").convert("RGBA")
          else:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottom.png").convert("RGBA")

          draw = ImageDraw.Draw(bottom)

          w, h = draw.textsize(str(images_names[inc_names]), font=font_name)
          draw.text((240, 83), str(images_prices[inc_names]), font=font_money, fill="white")
          draw.text(((512-w)/2, 15), images_names[inc_names], font=font_name, fill="white")

          back.paste(over, (0,0), over)

          background.paste(back, (0,0), back)

          background.paste(bottom, (0,512), bottom)

          final = image_to_byte(background)

        open(f"{os.path.dirname(os.path.abspath(__file__))}/images/final/{images_names[inc_names]}.png", "wb").write(final)

        inc_rarity += 1

      elif images_rarity[inc_rarity] == "uncommon" and images_series[inc_names] == None:

        over = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\objects\\{images_names[inc_names]}.png").convert("RGBA")

        if over.size == (1024, 1024): 

          font_money = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 84)

          font_name = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 90)

          back = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\UncommonXL.png").convert("RGBA")

          background = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\backgroundXL.png")

          if images_news[inc_names]:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottomXL-new.png").convert("RGBA")
          else:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottomXL.png").convert("RGBA")

          draw = ImageDraw.Draw(bottom)
          w, h = draw.textsize(str(images_names[inc_names]), font=font_name)
          draw.text((480, 170), str(images_prices[inc_names]), font=font_money, fill="white")
          draw.text(((1024-w)/2, 40), images_names[inc_names], font=font_name, fill="white")

          back.paste(over, (0,0), over)

          background.paste(back, (0,0), back)

          background.paste(bottom, (0,1024), bottom)

          final = image_to_byte(background)

        else:

          font_money = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 46)

          font_name = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 48)

          back = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\Uncommon.png").convert("RGBA")

          background = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\background.png")

          if images_news[inc_names]:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottom-new.png").convert("RGBA")
          else:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottom.png").convert("RGBA")

          draw = ImageDraw.Draw(bottom)

          w, h = draw.textsize(str(images_names[inc_names]), font=font_name)
          draw.text((240, 83), str(images_prices[inc_names]), font=font_money, fill="white")
          draw.text(((512-w)/2, 15), images_names[inc_names], font=font_name, fill="white")

          back.paste(over, (0,0), over)

          background.paste(back, (0,0), back)

          background.paste(bottom, (0,512), bottom)

          final = image_to_byte(background)

        open(f"{os.path.dirname(os.path.abspath(__file__))}/images/final/{images_names[inc_names]}.png", "wb").write(final)

        inc_rarity += 1

      elif images_rarity[inc_rarity] == "rare" and images_series[inc_names] == None:

        over = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\objects\\{images_names[inc_names]}.png").convert("RGBA")

        if over.size == (1024, 1024): 

          font_money = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 84)

          font_name = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 90)

          back = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\RareXL.png").convert("RGBA")

          background = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\backgroundXL.png")

          if images_news[inc_names]:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottomXL-new.png").convert("RGBA")
          else:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottomXL.png").convert("RGBA")

          draw = ImageDraw.Draw(bottom)
          w, h = draw.textsize(str(images_names[inc_names]), font=font_name)
          draw.text((480, 170), str(images_prices[inc_names]), font=font_money, fill="white")
          draw.text(((1024-w)/2, 40), images_names[inc_names], font=font_name, fill="white")

          back.paste(over, (0,0), over)

          background.paste(back, (0,0), back)

          background.paste(bottom, (0,1024), bottom)

          final = image_to_byte(background)

        else:

          font_money = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 46)

          font_name = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 48)

          back = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\Rare.png").convert("RGBA")

          background = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\background.png")

          if images_news[inc_names]:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottom-new.png").convert("RGBA")
          else:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottom.png").convert("RGBA")

          draw = ImageDraw.Draw(bottom)

          w, h = draw.textsize(str(images_names[inc_names]), font=font_name)
          draw.text((240, 83), str(images_prices[inc_names]), font=font_money, fill="white")
          draw.text(((512-w)/2, 15), images_names[inc_names], font=font_name, fill="white")

          back.paste(over, (0,0), over)

          background.paste(back, (0,0), back)

          background.paste(bottom, (0,512), bottom)

          final = image_to_byte(background)

        open(f"{os.path.dirname(os.path.abspath(__file__))}/images/final/{images_names[inc_names]}.png", "wb").write(final)

        inc_rarity += 1

      elif images_rarity[inc_rarity] == "epic" and images_series[inc_names] == None:

        over = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\objects\\{images_names[inc_names]}.png").convert("RGBA")

        if over.size == (1024, 1024): 

          font_money = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 84)

          font_name = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 90)

          back = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\EpicXL.png").convert("RGBA")

          background = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\backgroundXL.png")

          if images_news[inc_names]:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottomXL-new.png").convert("RGBA")
          else:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottomXL.png").convert("RGBA")

          draw = ImageDraw.Draw(bottom)
          w, h = draw.textsize(str(images_names[inc_names]), font=font_name)
          draw.text((480, 170), str(images_prices[inc_names]), font=font_money, fill="white")
          draw.text(((1024-w)/2, 40), images_names[inc_names], font=font_name, fill="white")

          back.paste(over, (0,0), over)

          background.paste(back, (0,0), back)

          background.paste(bottom, (0,1024), bottom)

          final = image_to_byte(background)

        else:

          font_money = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 46)

          font_name = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 48)

          back = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\Epic.png").convert("RGBA")

          background = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\background.png")

          if images_news[inc_names]:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottom-new.png").convert("RGBA")
          else:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottom.png").convert("RGBA")

          draw = ImageDraw.Draw(bottom)

          w, h = draw.textsize(str(images_names[inc_names]), font=font_name)
          draw.text((240, 83), str(images_prices[inc_names]), font=font_money, fill="white")
          draw.text(((512-w)/2, 15), images_names[inc_names], font=font_name, fill="white")

          back.paste(over, (0,0), over)

          background.paste(back, (0,0), back)

          background.paste(bottom, (0,512), bottom)

          final = image_to_byte(background)

        open(f"{os.path.dirname(os.path.abspath(__file__))}/images/final/{images_names[inc_names]}.png", "wb").write(final)

        inc_rarity += 1

      elif images_rarity[inc_rarity] == "legendary" and images_series[inc_names] == None:

        over = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\objects\\{images_names[inc_names]}.png").convert("RGBA")

        if over.size == (1024, 1024): 

          font_money = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 84)

          font_name = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 90)

          back = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\LegenXL.png").convert("RGBA")

          background = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\backgroundXL.png")

          if images_news[inc_names]:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottomXL-new.png").convert("RGBA")
          else:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottomXL.png").convert("RGBA")

          draw = ImageDraw.Draw(bottom)
          w, h = draw.textsize(str(images_names[inc_names]), font=font_name)
          draw.text((480, 170), str(images_prices[inc_names]), font=font_money, fill="white")
          draw.text(((1024-w)/2, 40), images_names[inc_names], font=font_name, fill="white")

          back.paste(over, (0,0), over)

          background.paste(back, (0,0), back)

          background.paste(bottom, (0,1024), bottom)

          final = image_to_byte(background)

        else:

          font_money = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 46)

          font_name = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 48)

          back = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\Legen.png").convert("RGBA")

          background = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\background.png")

          if images_news[inc_names]:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottom-new.png").convert("RGBA")
          else:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottom.png").convert("RGBA")

          draw = ImageDraw.Draw(bottom)

          w, h = draw.textsize(str(images_names[inc_names]), font=font_name)
          draw.text((240, 83), str(images_prices[inc_names]), font=font_money, fill="white")
          draw.text(((512-w)/2, 15), images_names[inc_names], font=font_name, fill="white")

          back.paste(over, (0,0), over)

          background.paste(back, (0,0), back)

          background.paste(bottom, (0,512), bottom)

          final = image_to_byte(background)

        open(f"{os.path.dirname(os.path.abspath(__file__))}/images/final/{images_names[inc_names]}.png", "wb").write(final)

        inc_rarity += 1

      elif images_series[inc_names] == "dc": 

        over = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\objects\\{images_names[inc_names]}.png").convert("RGBA")

        if over.size == (1024, 1024): 

          font_money = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 84)

          font_name = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 90)

          back = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\DcXL.png").convert("RGBA")

          background = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\backgroundXL.png")

          if images_news[inc_names]:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottomXL-new.png").convert("RGBA")
          else:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottomXL.png").convert("RGBA")

          draw = ImageDraw.Draw(bottom)
          w, h = draw.textsize(str(images_names[inc_names]), font=font_name)
          draw.text((480, 170), str(images_prices[inc_names]), font=font_money, fill="white")
          draw.text(((1024-w)/2, 40), images_names[inc_names], font=font_name, fill="white")

          back.paste(over, (0,0), over)

          background.paste(back, (0,0), back)

          background.paste(bottom, (0,1024), bottom)

          final = image_to_byte(background)

        else:

          font_money = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 46)

          font_name = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 48)

          back = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\Dc.png").convert("RGBA")

          background = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\background.png")

          if images_news[inc_names]:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottom-new.png").convert("RGBA")
          else:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottom.png").convert("RGBA")

          draw = ImageDraw.Draw(bottom)

          w, h = draw.textsize(str(images_names[inc_names]), font=font_name)
          draw.text((240, 83), str(images_prices[inc_names]), font=font_money, fill="white")
          draw.text(((512-w)/2, 15), images_names[inc_names], font=font_name, fill="white")

          back.paste(over, (0,0), over)

          background.paste(back, (0,0), back)

          background.paste(bottom, (0,512), bottom)

          final = image_to_byte(background)

        open(f"{os.path.dirname(os.path.abspath(__file__))}/images/final/{images_names[inc_names]}.png", "wb").write(final)
        inc_rarity += 1

      elif images_series[inc_names] == "marvel": 

        over = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\objects\\{images_names[inc_names]}.png").convert("RGBA")

        if over.size == (1024, 1024): 

          font_money = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 84)

          font_name = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 90)

          back = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\MarvelXL.png").convert("RGBA")

          background = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\backgroundXL.png")

          if images_news[inc_names]:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottomXL-new.png").convert("RGBA")
          else:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottomXL.png").convert("RGBA")

          draw = ImageDraw.Draw(bottom)
          w, h = draw.textsize(str(images_names[inc_names]), font=font_name)
          draw.text((480, 170), str(images_prices[inc_names]), font=font_money, fill="white")
          draw.text(((1024-w)/2, 40), images_names[inc_names], font=font_name, fill="white")

          back.paste(over, (0,0), over)

          background.paste(back, (0,0), back)

          background.paste(bottom, (0,1024), bottom)

          final = image_to_byte(background)

        else:

          font_money = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 46)

          font_name = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 48)

          back = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\Marvel.png").convert("RGBA")

          background = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\background.png")

          if images_news[inc_names]:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottom-new.png").convert("RGBA")
          else:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottom.png").convert("RGBA")

          draw = ImageDraw.Draw(bottom)

          w, h = draw.textsize(str(images_names[inc_names]), font=font_name)
          draw.text((240, 83), str(images_prices[inc_names]), font=font_money, fill="white")
          draw.text(((512-w)/2, 15), images_names[inc_names], font=font_name, fill="white")

          back.paste(over, (0,0), over)

          background.paste(back, (0,0), back)

          background.paste(bottom, (0,512), bottom)

          final = image_to_byte(background)

        open(f"{os.path.dirname(os.path.abspath(__file__))}/images/final/{images_names[inc_names]}.png", "wb").write(final)
        inc_rarity += 1

      elif images_series[inc_names] == "icon": 

        over = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\objects\\{images_names[inc_names]}.png").convert("RGBA")

        if over.size == (1024, 1024): 

          font_money = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 84)

          font_name = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 90)

          back = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\IconXL.png").convert("RGBA")

          background = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\backgroundXL.png")

          if images_news[inc_names]:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottomXL-new.png").convert("RGBA")
          else:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottomXL.png").convert("RGBA")

          draw = ImageDraw.Draw(bottom)
          w, h = draw.textsize(str(images_names[inc_names]), font=font_name)
          draw.text((480, 170), str(images_prices[inc_names]), font=font_money, fill="white")
          draw.text(((1024-w)/2, 40), images_names[inc_names], font=font_name, fill="white")

          back.paste(over, (0,0), over)

          background.paste(back, (0,0), back)

          background.paste(bottom, (0,1024), bottom)

          final = image_to_byte(background)

        else:

          font_money = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 46)

          font_name = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 48)

          back = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\Icon.png").convert("RGBA")

          background = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\background.png")

          if images_news[inc_names]:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottom-new.png").convert("RGBA")
          else:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottom.png").convert("RGBA")

          draw = ImageDraw.Draw(bottom)

          w, h = draw.textsize(str(images_names[inc_names]), font=font_name)
          draw.text((240, 83), str(images_prices[inc_names]), font=font_money, fill="white")
          draw.text(((512-w)/2, 15), images_names[inc_names], font=font_name, fill="white")

          back.paste(over, (0,0), over)

          background.paste(back, (0,0), back)

          background.paste(bottom, (0,512), bottom)

          final = image_to_byte(background)

        open(f"{os.path.dirname(os.path.abspath(__file__))}/images/final/{images_names[inc_names]}.png", "wb").write(final)
        inc_rarity += 1

      elif images_series[inc_names] == "dark": 

        over = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\objects\\{images_names[inc_names]}.png").convert("RGBA")

        if over.size == (1024, 1024): 

          font_money = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 84)

          font_name = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 90)

          back = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\DarkXL.png").convert("RGBA")

          background = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\backgroundXL.png")

          if images_news[inc_names]:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottomXL-new.png").convert("RGBA")
          else:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottomXL.png").convert("RGBA")

          draw = ImageDraw.Draw(bottom)
          w, h = draw.textsize(str(images_names[inc_names]), font=font_name)
          draw.text((480, 170), str(images_prices[inc_names]), font=font_money, fill="white")
          draw.text(((1024-w)/2, 40), images_names[inc_names], font=font_name, fill="white")

          back.paste(over, (0,0), over)

          background.paste(back, (0,0), back)

          background.paste(bottom, (0,1024), bottom)

          final = image_to_byte(background)

        else:

          font_money = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 46)

          font_name = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 48)

          back = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\Dark.png").convert("RGBA")

          background = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\background.png")

          if images_news[inc_names]:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottom-new.png").convert("RGBA")
          else:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottom.png").convert("RGBA")

          draw = ImageDraw.Draw(bottom)

          w, h = draw.textsize(str(images_names[inc_names]), font=font_name)
          draw.text((240, 83), str(images_prices[inc_names]), font=font_money, fill="white")
          draw.text(((512-w)/2, 15), images_names[inc_names], font=font_name, fill="white")

          back.paste(over, (0,0), over)

          background.paste(back, (0,0), back)

          background.paste(bottom, (0,512), bottom)

          final = image_to_byte(background)

        open(f"{os.path.dirname(os.path.abspath(__file__))}/images/final/{images_names[inc_names]}.png", "wb").write(final)
        inc_rarity += 1

      elif images_series[inc_names] == "shadow": 

        over = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\objects\\{images_names[inc_names]}.png").convert("RGBA")

        if over.size == (1024, 1024): 

          font_money = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 84)

          font_name = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 90)

          back = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\ShadowXL.png").convert("RGBA")

          background = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\backgroundXL.png")

          if images_news[inc_names]:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottomXL-new.png").convert("RGBA")
          else:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottomXL.png").convert("RGBA")

          draw = ImageDraw.Draw(bottom)
          w, h = draw.textsize(str(images_names[inc_names]), font=font_name)
          draw.text((480, 170), str(images_prices[inc_names]), font=font_money, fill="white")
          draw.text(((1024-w)/2, 40), images_names[inc_names], font=font_name, fill="white")

          back.paste(over, (0,0), over)

          background.paste(back, (0,0), back)

          background.paste(bottom, (0,1024), bottom)

          final = image_to_byte(background)

        else:

          font_money = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 46)

          font_name = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 48)

          back = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\Shadow.png").convert("RGBA")

          background = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\background.png")

          if images_news[inc_names]:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottom-new.png").convert("RGBA")
          else:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottom.png").convert("RGBA")

          draw = ImageDraw.Draw(bottom)

          w, h = draw.textsize(str(images_names[inc_names]), font=font_name)
          draw.text((240, 83), str(images_prices[inc_names]), font=font_money, fill="white")
          draw.text(((512-w)/2, 15), images_names[inc_names], font=font_name, fill="white")

          back.paste(over, (0,0), over)

          background.paste(back, (0,0), back)

          background.paste(bottom, (0,512), bottom)

          final = image_to_byte(background)

        open(f"{os.path.dirname(os.path.abspath(__file__))}/images/final/{images_names[inc_names]}.png", "wb").write(final)
        inc_rarity += 1

      elif images_series[inc_names] == "frozen": 

        over = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\objects\\{images_names[inc_names]}.png").convert("RGBA")

        if over.size == (1024, 1024): 

          font_money = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 84)

          font_name = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 90)

          back = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\FrozenXL.png").convert("RGBA")

          background = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\backgroundXL.png")

          if images_news[inc_names]:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottomXL-new.png").convert("RGBA")
          else:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottomXL.png").convert("RGBA")

          draw = ImageDraw.Draw(bottom)
          w, h = draw.textsize(str(images_names[inc_names]), font=font_name)
          draw.text((480, 170), str(images_prices[inc_names]), font=font_money, fill="white")
          draw.text(((1024-w)/2, 40), images_names[inc_names], font=font_name, fill="white")

          back.paste(over, (0,0), over)

          background.paste(back, (0,0), back)

          background.paste(bottom, (0,1024), bottom)

          final = image_to_byte(background)

        else:

          font_money = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 46)

          font_name = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 48)

          back = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\Frozen.png").convert("RGBA")

          background = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\background.png")

          if images_news[inc_names]:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottom-new.png").convert("RGBA")
          else:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottom.png").convert("RGBA")

          draw = ImageDraw.Draw(bottom)

          w, h = draw.textsize(str(images_names[inc_names]), font=font_name)
          draw.text((240, 83), str(images_prices[inc_names]), font=font_money, fill="white")
          draw.text(((512-w)/2, 15), images_names[inc_names], font=font_name, fill="white")

          back.paste(over, (0,0), over)

          background.paste(back, (0,0), back)

          background.paste(bottom, (0,512), bottom)

          final = image_to_byte(background)

        open(f"{os.path.dirname(os.path.abspath(__file__))}/images/final/{images_names[inc_names]}.png", "wb").write(final)
        inc_rarity += 1

      elif images_series[inc_names] == "slurpseries": 

        over = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\objects\\{images_names[inc_names]}.png").convert("RGBA")

        if over.size == (1024, 1024): 

          font_money = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 84)

          font_name = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 90)

          back = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\SlurpseriesXL.png").convert("RGBA")

          background = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\backgroundXL.png")

          if images_news[inc_names]:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottomXL-new.png").convert("RGBA")
          else:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottomXL.png").convert("RGBA")

          draw = ImageDraw.Draw(bottom)
          w, h = draw.textsize(str(images_names[inc_names]), font=font_name)
          draw.text((480, 170), str(images_prices[inc_names]), font=font_money, fill="white")
          draw.text(((1024-w)/2, 40), images_names[inc_names], font=font_name, fill="white")

          back.paste(over, (0,0), over)

          background.paste(back, (0,0), back)

          background.paste(bottom, (0,1024), bottom)

          final = image_to_byte(background)

        else:

          font_money = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 46)

          font_name = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 48)

          back = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\Slurpseries.png").convert("RGBA")

          background = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\background.png")

          if images_news[inc_names]:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottom-new.png").convert("RGBA")
          else:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottom.png").convert("RGBA")

          draw = ImageDraw.Draw(bottom)

          w, h = draw.textsize(str(images_names[inc_names]), font=font_name)
          draw.text((240, 83), str(images_prices[inc_names]), font=font_money, fill="white")
          draw.text(((512-w)/2, 15), images_names[inc_names], font=font_name, fill="white")

          back.paste(over, (0,0), over)

          background.paste(back, (0,0), back)

          background.paste(bottom, (0,512), bottom)

          final = image_to_byte(background)

        open(f"{os.path.dirname(os.path.abspath(__file__))}/images/final/{images_names[inc_names]}.png", "wb").write(final)
        inc_rarity += 1

      elif images_series[inc_names] == "starwars": 

        over = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\objects\\{images_names[inc_names]}.png").convert("RGBA")

        if over.size == (1024, 1024): 

          font_money = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 84)

          font_name = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 90)

          back = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\StarwarsXL.png").convert("RGBA")

          background = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\backgroundXL.png")

          if images_news[inc_names]:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottomXL-new.png").convert("RGBA")
          else:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottomXL.png").convert("RGBA")

          draw = ImageDraw.Draw(bottom)
          w, h = draw.textsize(str(images_names[inc_names]), font=font_name)
          draw.text((480, 170), str(images_prices[inc_names]), font=font_money, fill="white")
          draw.text(((1024-w)/2, 40), images_names[inc_names], font=font_name, fill="white")

          back.paste(over, (0,0), over)

          background.paste(back, (0,0), back)

          background.paste(bottom, (0,1024), bottom)

          final = image_to_byte(background)

        else:

          font_money = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 46)

          font_name = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 48)

          back = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\Starwars.png").convert("RGBA")

          background = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\background.png")

          if images_news[inc_names]:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottom-new.png").convert("RGBA")
          else:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottom.png").convert("RGBA")

          draw = ImageDraw.Draw(bottom)

          w, h = draw.textsize(str(images_names[inc_names]), font=font_name)
          draw.text((240, 83), str(images_prices[inc_names]), font=font_money, fill="white")
          draw.text(((512-w)/2, 15), images_names[inc_names], font=font_name, fill="white")

          back.paste(over, (0,0), over)

          background.paste(back, (0,0), back)

          background.paste(bottom, (0,512), bottom)

          final = image_to_byte(background)

        open(f"{os.path.dirname(os.path.abspath(__file__))}/images/final/{images_names[inc_names]}.png", "wb").write(final)
        inc_rarity += 1

      elif images_series[inc_names] == "platform": 

        over = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\objects\\{images_names[inc_names]}.png").convert("RGBA")

        if over.size == (1024, 1024): 

          font_money = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 84)

          font_name = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 90)

          back = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\PlatformXL.png").convert("RGBA")

          background = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\backgroundXL.png")

          if images_news[inc_names]:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottomXL-new.png").convert("RGBA")
          else:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottomXL.png").convert("RGBA")

          draw = ImageDraw.Draw(bottom)
          w, h = draw.textsize(str(images_names[inc_names]), font=font_name)
          draw.text((480, 170), str(images_prices[inc_names]), font=font_money, fill="white")
          draw.text(((1024-w)/2, 40), images_names[inc_names], font=font_name, fill="white")

          back.paste(over, (0,0), over)

          background.paste(back, (0,0), back)

          background.paste(bottom, (0,1024), bottom)

          final = image_to_byte(background)

        else:

          font_money = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 46)

          font_name = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 48)

          back = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\Platform.png").convert("RGBA")

          background = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\background.png")

          if images_news[inc_names]:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottom-new.png").convert("RGBA")
          else:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottom.png").convert("RGBA")

          draw = ImageDraw.Draw(bottom)

          w, h = draw.textsize(str(images_names[inc_names]), font=font_name)
          draw.text((240, 83), str(images_prices[inc_names]), font=font_money, fill="white")
          draw.text(((512-w)/2, 15), images_names[inc_names], font=font_name, fill="white")

          back.paste(over, (0,0), over)

          background.paste(back, (0,0), back)

          background.paste(bottom, (0,512), bottom)

          final = image_to_byte(background)

        open(f"{os.path.dirname(os.path.abspath(__file__))}/images/final/{images_names[inc_names]}.png", "wb").write(final)
        inc_rarity += 1

      elif images_series[inc_names] == "lava": 

        over = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\objects\\{images_names[inc_names]}.png").convert("RGBA")

        if over.size == (1024, 1024): 

          font_money = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 84)

          font_name = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 90)

          back = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\LavaXL.png").convert("RGBA")

          background = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\backgroundXL.png")

          if images_news[inc_names]:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottomXL-new.png").convert("RGBA")
          else:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottomXL.png").convert("RGBA")

          draw = ImageDraw.Draw(bottom)
          w, h = draw.textsize(str(images_names[inc_names]), font=font_name)
          draw.text((480, 170), str(images_prices[inc_names]), font=font_money, fill="white")
          draw.text(((1024-w)/2, 40), images_names[inc_names], font=font_name, fill="white")

          back.paste(over, (0,0), over)

          background.paste(back, (0,0), back)

          background.paste(bottom, (0,1024), bottom)

          final = image_to_byte(background)

        else:

          font_money = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 46)

          font_name = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\Fortnite.ttf", 48)

          back = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\Lava.png").convert("RGBA")

          background = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\background.png")

          if images_news[inc_names]:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottom-new.png").convert("RGBA")
          else:
            bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\presets\\bottom.png").convert("RGBA")

          draw = ImageDraw.Draw(bottom)

          w, h = draw.textsize(str(images_names[inc_names]), font=font_name)
          draw.text((240, 83), str(images_prices[inc_names]), font=font_money, fill="white")
          draw.text(((512-w)/2, 15), images_names[inc_names], font=font_name, fill="white")

          back.paste(over, (0,0), over)

          background.paste(back, (0,0), back)

          background.paste(bottom, (0,512), bottom)

          final = image_to_byte(background)

        open(f"{os.path.dirname(os.path.abspath(__file__))}/images/final/{images_names[inc_names]}.png", "wb").write(final)
        inc_rarity += 1

      inc_names+=1

    except IndexError: 
      break

def resize_images(dir_img, size):

  flag1 = True
  flag2 = False
  flag3 = False
  list1 = []
  list2 = []
  list3 = []
  list4 = []
  list5 = []
  inc = 0

  for i in dir_img: 

    dir_img[inc] = f"{os.path.dirname(os.path.abspath(__file__))}\\images\\final\\{i}"
    ap = cv2.imread(dir_img[inc])
    ap = cv2.resize(ap, size)


    if flag1 and not flag2 and not flag3: # V, F, F
      list1.append(ap)
      flag1 = False


    elif not flag1 and not flag2 and not flag3: # F, F, F
      list2.append(ap)
      flag2 = True

    
    elif not flag1 and flag2: # F, V
      list3.append(ap)
      flag2 = False
      flag3 = True


    elif not flag1 and not flag2 and flag3: # F, F, V
      list4.append(ap)
      flag1 = True
      flag2 = True
      flag3 = False


    elif flag1 and flag2 and not flag3: # V, V, F
      list5.append(ap)
      flag1 = True
      flag2 = False
      flag3 = False


    inc+=1


  concat = cv2.hconcat(list1)
  concat2 = cv2.hconcat(list2)
  concat3 = cv2.hconcat(list3)
  concat4 = cv2.hconcat(list4)
  concat5 = cv2.hconcat(list5)


  return concat, concat2, concat3, concat4, concat5