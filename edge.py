# import python image library
from PIL import Image, ImageFilter

#opening demo image
img = Image.open('demo.jpg')

#finding edge in image
edge = img.filter(ImageFilter.FIND_EDGES())

#displaying image with edges
edge.show()