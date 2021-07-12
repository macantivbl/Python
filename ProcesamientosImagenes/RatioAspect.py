from PIL import Image, ImageFilter

img = Image.open('astro.jpg')
new_img = img.thumbnail((400,200))
img.save('thmn.jpg')
img.show()

print(img.size)