from PIL import Image

#img = Image.new("RGB",(640,480),(0,0,255))


background = Image.open("cat1.png")
foreground = Image.open("cat2.png")
background.paste(foreground, (0, 0), foreground)

foreground = Image.open("cat3.png")
background.paste(foreground, (0, 0), foreground)

background.show()	