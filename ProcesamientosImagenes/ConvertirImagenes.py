from PIL import Image, ImageFilter

img = Image.open('pikachu.jpg')

filter_img = img.convert('L')
filter_img.save('grey.png','png')
filter_img.show()
rotar = filter_img.rotate(90)
rotar.save('pikaRotar.png','png')
rotar.show()
rezise = filter_img.resize((300,300))
rezise.save("PikaPequeño.png",'png')
rezise.show()
box = (100,100,400,400)
region = img.crop(box)
region.save("PikaRecortado.png","png")
region.show()