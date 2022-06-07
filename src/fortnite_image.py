import io
import os
import requests
from PIL import Image, ImageDraw, ImageFont
import cv2

class FortniteImage:

  def create_image_store(self):

    url = "https://fortnite-api.theapinetwork.com/store/get"
    req = requests.get(url)
    data = req.json()

    count = 0
    images_links, images_names, images_rarity, images_prices, images_series, images_news = [], [], [], [], [], []

    self.__clean_images_folder(f"{os.path.dirname(os.path.abspath(__file__))}\\assets\\images\\final")
    self.__clean_images_folder(f"{os.path.dirname(os.path.abspath(__file__))}\\assets\\images\\objects")
    

    for i in data["data"]: 

      count += 1

      # Choose the complete image else choose the icon image
      if i["item"]["images"]["featured"] != None and i["item"]["type"] == "outfit":
        item_image = i["item"]["images"]["featured"]
      else:
        item_image = i["item"]["images"]["icon"]
      
      item_name = i["item"]["name"]
      item_rarity = i["item"]["rarity"]
      item_serie = i["item"]["series"]
      item_price = i["store"]["cost"]
      isNew = i["store"]["isNew"]
    
      images_links.append(item_image)
      images_names.append(item_name)
      images_rarity.append(item_rarity)
      images_prices.append(item_price)
      images_series.append(item_serie)
      images_news.append(isNew)


    # Create the final image and store it in the folder
    self.__create_final_images(images_links, images_names, images_rarity, images_prices, images_series, images_news)

    final_images = os.listdir(f"{os.path.dirname(os.path.abspath(__file__))}\\assets\\images\\final")

    # Resize the images that are stored
    images_row, images_row2, images_row3, images_row4, images_row5 = self.__concat_images(final_images)

    images_row, images_row2, images_row3, images_row4, images_row5 = self.__create_empty_image(images_row, images_row2, images_row3, images_row4, images_row5)

    print()

    if(len(images_row) >= 400):
      shop_image1 = cv2.vconcat([images_row, images_row2, images_row3])
      shop_image2 = cv2.vconcat([images_row4, images_row5])

      cv2.imwrite(f"{os.path.dirname(os.path.abspath(__file__))}/assets/images/shop/shop1.png", shop_image1)
      cv2.imwrite(f"{os.path.dirname(os.path.abspath(__file__))}/assets/images/shop/shop2.png", shop_image2)
      return False


    shop_image = cv2.vconcat([images_row, images_row2, images_row3, images_row4, images_row5])

    cv2.imwrite(f"{os.path.dirname(os.path.abspath(__file__))}/assets/images/shop/shop.png", shop_image)

    return True

  def __create_empty_image(self, images_row, images_row2, images_row3, images_row4, images_row5):
    # Add black images to the arrays when the array has a image less
    # Subtracting the concat1 shape with less shape

    size_empty = images_row.shape[1] - images_row5.shape[1]
    empty_amount = int(size_empty / 512)
    empty_img = cv2.imread(f"{os.path.dirname(os.path.abspath(__file__))}/assets/images/presets/Empty.png")
    empty_img = cv2.resize(empty_img, (512, 660))
    
    for i in range(0, empty_amount):
      
      if images_row.shape != images_row2.shape:
        images_row2 = cv2.hconcat([images_row2, empty_img])

      if images_row.shape != images_row3.shape:
        images_row3 = cv2.hconcat([images_row3, empty_img])

      if images_row.shape != images_row4.shape:
        images_row4 = cv2.hconcat([images_row4, empty_img])

      if images_row.shape != images_row5.shape:
        images_row5 = cv2.hconcat([images_row5, empty_img])
        

    return images_row, images_row2, images_row3, images_row4, images_row5

  def __concat_images(self, final_images):

    flags = {
      "flag1": True,
      "flag2": False,
      "flag3": False
    }

    lists = {
      "list1": [],
      "list2": [],
      "list3": [],
      "list4": [],
      "list5": []
    }

    count = 0

    for final_image in final_images:

      final_image = cv2.imread(f"{os.path.dirname(os.path.abspath(__file__))}/assets/images/final/{final_image}")
            
      if flags["flag1"] and not flags["flag2"] and not flags["flag3"]:  # V, F, F
        lists["list1"].append(final_image)
        flags["flag1"] = False

      elif not flags["flag1"] and not flags["flag2"] and not flags["flag3"]:  # F, F, F
        lists["list2"].append(final_image)
        flags["flag2"] = True

      elif not flags["flag1"] and flags["flag2"]:  # F, V
        lists["list3"].append(final_image)
        flags["flag2"] = False
        flags["flag3"] = True

      elif not flags["flag1"] and not flags["flag2"] and flags["flag3"]:  # F, F, V
        lists["list4"].append(final_image)
        flags["flag1"] = True
        flags["flag2"] = True
        flags["flag3"] = False

      elif flags["flag1"] and flags["flag2"] and not flags["flag3"]:  # V, V, F
        lists["list5"].append(final_image)
        flags["flag1"] = True
        flags["flag2"] = False
        flags["flag3"] = False

      count += 1


    images_row = cv2.hconcat(lists["list1"])
    images_row2 = cv2.hconcat(lists["list2"])
    images_row3 = cv2.hconcat(lists["list3"])
    images_row4 = cv2.hconcat(lists["list4"])
    images_row5 = cv2.hconcat(lists["list5"])


    return images_row, images_row2, images_row3, images_row4, images_row5

  def __image_to_byte(self, image):
    img_byte_array = io.BytesIO()
    image.save(img_byte_array, format=image.format)
    img_byte_array = img_byte_array.getvalue()

    return img_byte_array

  def __clean_images_folder(self, folder_path):
    images_in_the_folder = os.listdir(folder_path)
    for i in images_in_the_folder:
      os.remove(f"{folder_path}\\{i}")
    
  def __create_final_images(self, images_links, images_names, images_rarity, images_prices, images_series, images_news):

    count = 0

    for image_link in images_links:

      try:

        image_response = requests.get(image_link)
        open(f"{os.path.dirname(os.path.abspath(__file__))}/assets/images/objects/{images_names[count]}.png", "wb").write(image_response.content)
        item_image = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\assets\\images\\objects\\{images_names[count]}.png")
        
        item_image = item_image.resize((512, 512))

        images = {
          "item": item_image,
          "serie": images_series[count],
          "rarity": images_rarity[count],
          "name": images_names[count],
          "price": images_prices[count],
          "new": images_news[count]
        }
      
        backgroundShop = self.__get_final_image(images=images)
        final_image = self.__image_to_byte(backgroundShop)

        open(f"{os.path.dirname(os.path.abspath(__file__))}/assets/images/final/{images_names[count]}.png", "wb").write(final_image)


        count += 1

      except IndexError:
        raise Exception(f"Error: someting went wrong with the creation of the final image with link: {image_link}")

  def __get_final_image(self, images):

    rarity = self.__get_rarity_formatted(images["rarity"] if images["serie"] == None else images["serie"])

    font_money = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\assets\\fonts\\Fortnite.ttf", 46)
    font_name = ImageFont.truetype(f"{os.path.dirname(os.path.abspath(__file__))}\\assets\\fonts\\Fortnite.ttf", 48)
    backgroundRarity = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\assets\\images\\presets\\{rarity}.png").convert("RGBA")
    backgroundShop = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\assets\\images\\presets\\background.png")

    if images["new"]:
      bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\assets\\images\\presets\\bottom-new.png").convert("RGBA")
    else:
      bottom = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\assets\\images\\presets\\bottom.png").convert("RGBA")

    draw = ImageDraw.Draw(bottom)
    width, _ = draw.textsize(str(images["name"]), font=font_name)
    draw.text((240, 83), str(images["price"]), font=font_money, fill="white")
    draw.text(((512 - width) / 2, 15), images["name"], font=font_name, fill="white")

    backgroundRarity.paste(images["item"], (0, 0), images["item"])

    backgroundShop.paste(backgroundRarity, (0, 0), backgroundRarity)

    backgroundShop.paste(bottom, (0, 512), bottom)

    return backgroundShop

  def __get_rarity_formatted(self, rarity):

    if rarity == "common":
      return "Common"
    elif rarity == "uncommon":
      return "Uncommon"
    elif rarity == "rare":
      return "Rare"
    elif rarity == "epic":
      return "Epic"
    elif rarity == "legendary":
      return "Legen"
    elif rarity == "dark":
      return "Dark"
    elif rarity == "dc":
      return "Dc"
    elif rarity == "frozen":
      return "Frozen"
    elif rarity == "shadow":
      return "Shadow"
    elif rarity == "icon":
      return "Icon"
    elif rarity == "lava":
      return "Lava"
    elif rarity == "slurpseries":
      return "Slurpseries"
    elif rarity == "starwars":
      return "Starwars"
    elif rarity == "platform":
      return "Platform"
    elif rarity == "marvel":
      return "Marvel"