# import python image library
from PIL import Image, ImageFilter

#opening demo image
img = Image.open('demo.jpg')
#displaying demo image
img.show()

#finding edge in image
edge = img.filter(ImageFilter.FIND_EDGES())
#displaying image with edges
edge.show()


#getting width and height of image
width, height = img.size

#changing value of each pixel by negative color
for x in range(width):
    for y in range(height):
        
        pixel_coordinate = (x,y)
        r, g, b = img.getpixel(pixel_coordinate)
        
        neg_color = (255 - r, 255 - g, 255 - b)
        img.putpixel( pixel_coordinate, neg_color)
img.show()