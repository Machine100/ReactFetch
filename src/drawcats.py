from PIL import Image

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

mainimage = Image.open("house1.png")

imgfood1 = Image.open("food1.png")  
imgfood2 = Image.open("food2.png")
imgtoy1  = Image.open("toy1.png")
imgtoy2  = Image.open("toy2.png")
imgtoy3  = Image.open("toy3.png")
imgcat1  = Image.open("cat1.png")
imgcat2  = Image.open("cat2.png")
imgcat3  = Image.open("cat3.png")
imgcat4  = Image.open("cat4.png")
imgcat5  = Image.open("cat5.png")

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