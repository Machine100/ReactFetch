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

food1 = Image.open("food1.png")  
food2 = Image.open("food2.png")
toy1  = Image.open("toy1.png")
toy2  = Image.open("toy2.png")
toy3  = Image.open("toy3.png")
cat1  = Image.open("cat1.png")
cat2  = Image.open("cat2.png")
cat3  = Image.open("cat3.png")
cat4  = Image.open("cat4.png")
cat5  = Image.open("cat5.png")

#mainimage.show()
if event[food1]:
	mainimage.paste(food1, (0, 0), food1)
if event[food2]:
	mainimage.paste(food2, (0, 0), food2)
if event[toy1]:
	mainimage.paste(toy1,  (0, 0), toy1)
if event[toy2]:
	mainimage.paste(toy2,  (0, 0), toy2)
if event[toy3]:
	mainimage.paste(toy3,  (0, 0), toy3)
if event[cat1]:
	mainimage.paste(cat1,  (0, 0), cat1)
if event[cat2]:
	mainimage.paste(cat2,  (0, 0), cat2)
if event[cat3]:
	mainimage.paste(cat3,  (0, 0), cat3)
if event[cat4]:
	mainimage.paste(cat4,  (0, 0), cat4)
if event[cat5]:
	mainimage.paste(cat5,  (0, 0), cat5)

mainimage.show()

#background = Image.open("house1.png")
#foreground = Image.open("house2.png")
#background.paste(foreground, (0, 0), foreground)
#background.show()	