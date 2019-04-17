from PIL import Image
import requests
from io import BytesIO

event = {"food1": True, 
         "food2": True, 
         "toy1": True,
         "toy2": True,
         "toy3": False,
         "cat1": True,
         "cat2": False,
         "cat3": True,
         "cat4": False,
         "cat5": True}

house1url = "https://s3.amazonaws.com/derffred/house1.png"
food1url  = "https://s3.amazonaws.com/derffred/food1.png"
food2url  = "https://s3.amazonaws.com/derffred/food2.png"
toy1url   = "https://s3.amazonaws.com/derffred/toy1.png"
toy2url   = "https://s3.amazonaws.com/derffred/toy2.png"
toy3url   = "https://s3.amazonaws.com/derffred/toy3.png"
cat1url   = "https://s3.amazonaws.com/derffred/cat1.png"
cat2url   = "https://s3.amazonaws.com/derffred/cat2.png"
cat3url   = "https://s3.amazonaws.com/derffred/cat3.png"
cat4url   = "https://s3.amazonaws.com/derffred/cat4.png"
cat5url   = "https://s3.amazonaws.com/derffred/cat5.png"

house1response = requests.get(house1url)
food1response = requests.get(house1url)
food2response = requests.get(house1url)
toy1response = requests.get(house1url)
toy2response = requests.get(house1url)
toy3response = requests.get(house1url)
cat1response = requests.get(house1url)
cat2response = requests.get(house1url)
cat3response = requests.get(house1url)
cat4response = requests.get(house1url)
cat5response = requests.get(house1url)

mainimage = Image.open(BytesIO(house1response.content))
imgfood1 =  Image.open(BytesIO(food1response.content))  
imgfood2 =  Image.open(BytesIO(food2response.content))
imgtoy1  =  Image.open(BytesIO(toy1response.content))
imgtoy2  =  Image.open(BytesIO(toy2response.content))
imgtoy3  =  Image.open(BytesIO(toy3response.content))
imgcat1  =  Image.open(BytesIO(cat1response.content))
imgcat2  =  Image.open(BytesIO(cat2response.content))
imgcat3  =  Image.open(BytesIO(cat3response.content))
imgcat4  =  Image.open(BytesIO(cat4response.content))
imgcat5  =  Image.open(BytesIO(cat5response.content))

if event['food1']:
	mainimage.paste(imgfood1, (0, 0), imgfood1)
if event['food2']:
	mainimage.paste(imgfood2, (0, 0), imgfood2)
if event['toy1']:
	mainimage.paste(imgtoy1,  (0, 0), imgtoy1)
if event['toy2']:
	mainimage.paste(imgtoy2,  (0, 0), imgtoy2)
if event['toy3']:
	mainimage.paste(imgtoy3,  (0, 0), imgtoy3)
if event['cat1']:
	mainimage.paste(imgcat1,  (0, 0), imgcat1)
if event['cat2']:
	mainimage.paste(imgcat2,  (0, 0), imgcat2)
if event['cat3']:
	mainimage.paste(imgcat3,  (0, 0), imgcat3)
if event['cat4']:
	mainimage.paste(imgcat4,  (0, 0), imgcat4)
if event['cat5']:
	mainimage.paste(imgcat5,  (0, 0), imgcat5)

mainimage.show()

#background = Image.open("house1.png")
#foreground = Image.open("house2.png")
#background.paste(foreground, (0, 0), foreground)
#background.show()	