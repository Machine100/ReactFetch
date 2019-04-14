from PIL import Image

#img = Image.new("RGB",(640,480),(0,0,255))


background = Image.open("house1.png")
foreground = Image.open("house2.png")
background.paste(foreground, (0, 0), foreground)



background.show()	