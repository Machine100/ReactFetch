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


if state[]:
	mainimage.paste(food1, (0, 0), food1)
if state[]:
	mainimage.paste(food2, (0, 0), food2)
if state[]:
	mainimage.paste(toy1,  (0, 0), toy1)
if state[]:
	mainimage.paste(toy2,  (0, 0), toy2)
if state[]:
	mainimage.paste(toy3,  (0, 0), toy3)
if state[]:
	mainimage.paste(cat1,  (0, 0), cat1)
if state[]:
	mainimage.paste(cat2,  (0, 0), cat2)
if state[]:
	mainimage.paste(cat3,  (0, 0), cat3)
if state[]:
	mainimage.paste(cat4,  (0, 0), cat4)
if state[]:
	mainimage.paste(cat5,  (0, 0), cat5)

background = Image.open("house1.png")
foreground = Image.open("house2.png")
background.paste(foreground, (0, 0), foreground)

background.show()	