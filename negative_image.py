#getting width and height of image
width, height = img.size

#changing value of each pixel by negative color
for x in range(width):
    for y in range(height):
        
        pixel_coordinate = (x,y)
        #getting rgb value of a pixel
	r, g, b = img.getpixel(pixel_coordinate)
        
        #negativing the pixel 
	neg_color = (255 - r, 255 - g, 255 - b)
        #changing rgb of pixels with new value
	img.putpixel( pixel_coordinate, neg_color)
img.show()