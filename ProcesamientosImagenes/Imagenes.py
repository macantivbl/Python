from PIL import Image, ImageFilter

img = Image.open('pikachu.jpg')

print(img.format)
print(img.size)
print(img.mode)
filter_img = img.filter(ImageFilter.BLUR)
#https://pillow.readthedocs.io/en/stable/
filter_img.save("blur.png",'png')