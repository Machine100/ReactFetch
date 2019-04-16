from PIL import Image

mainimage = Image.open("")

food1 = Image.open("")  
food2 = Image.open("")
toy1  = Image.open("")
toy2  = Image.open("")
toy3  = Image.open("")
cat1  = Image.open("")
cat2  = Image.open("")
cat3  = Image.open("")
cat4  = Image.open("")
cat5  = Image.open("")


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