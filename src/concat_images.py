import requests
import cv2
import os
from PIL import Image
from utils import create_final_image, create_empty_image, resize_images


async def create_image_store():

  url = "https://fortnite-api.theapinetwork.com/store/get"

  req = requests.get(url)

  data = req.json()
  inc = 0

  images_raw = []
  images_names = []
  images_rarity = []
  images_prices = []
  images_series = []
  images_news = []

  # Limpia las carpetas antes de traer nuevas
  clean_img = os.listdir(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\final")

  for i in clean_img:

    os.remove(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\final\\{i}")
    os.remove(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\objects\\{i}")

  for i in data["data"]: 

    inc+=1

    if i["item"]["images"]["featured"] != None and i["item"]["type"] == "outfit":
      image = i["item"]["images"]["featured"]
    else:
      image = i["item"]["images"]["icon"]
    
    name = i["item"]["name"]
    rarity = i["item"]["rarity"]
    serie = i["item"]["series"]
    price = i["store"]["cost"]
    new = i["store"]["isNew"]
  

    images_raw.append(image)
    images_names.append(name)
    images_rarity.append(rarity)
    images_prices.append(price)
    images_series.append(serie)
    images_news.append(new)


  # Crea la imagen final y la guarda en la carpeta
  create_final_image(images_raw, images_names, images_rarity, images_prices, images_series, images_news)


  img = os.listdir(f"{os.path.dirname(os.path.abspath(__file__))}\\images\\final")

  # Redimenciona las imagenes que estan guardadas
  concat, concat2, concat3, concat4, concat5 = resize_images(img, (512, 660))

  # Calcula los arreglosp para rellenar con imagenes negras los espacios vacios
  concat, concat2, concat3, concat4, concat5 = create_empty_image(concat, concat2, concat3, concat4, concat5)

  """ print(concat.shape)
  print(concat2.shape)
  print(concat3.shape)
  print(concat4.shape)
  print(concat5.shape) """

  concat_v = cv2.vconcat([concat2, concat3, concat, concat4, concat5])

  cv2.imwrite(f"{os.path.dirname(os.path.abspath(__file__))}/images/shop/shop.png",concat_v)

  print("READY")

