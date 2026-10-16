from PIL import Image
import ulterate as ult
import heightmap

# classes

class Pixel:
    def __init__(self, r, g, b, x, y):
        self.r = r
        self.g = g
        self.b = b
        
        self.color = (self.r, self.g, self.b)
        
        self.x = x
        self.y = y
        
    def set_color(self):
        self.color = (self.r, self.g, self.b)
    
    


# variables

pixels = []
pixelcount = 0

img_path = "assets/" + str(input("input the name of the file in the assets folder (-> filename.sufix <-): "))

img = Image.open(img_path)
width, height = img.size


def get_pixels(img_path):
    global pixels, pixelcount

    img = Image.open(img_path)

    width, height = img.size
    
    for y in range(height):
        for x in range(width):
            
            if img.mode == 'RGB':
                r, g, b = img.getpixel((x, y))
            
            elif img.mode == 'RGBA':
                r, g, b, a = img.getpixel((x, y))
            
            pixel = Pixel(r, g, b, x, y)
            pixels.append(pixel)
            pixelcount += 1
            
    print(f'{pixelcount} pixels analised')
    
                        
def new_image(width, height):
    output_img = Image.new("RGB", (width, height), color = (0,0,0))
    
    for pixel in pixels:
        output_img.putpixel((pixel.x, pixel.y), pixel.color)
        
    output_img.save("output/result.png")
    
    
def mode(pixels):
    global width
    
    allowed_answers = ['1', '2', '3', '4', '5', '6', '7']
    in_mode: str = None
    
    while not in_mode in allowed_answers:
        in_mode = str(input('\nChose your option (-> number <-): \n(1) pure RGB\n(2) Black and White \n(3) Random Color \n(4) Invert \n(5) Half invertied \n(6) single channel \n(7) colored heightmap \nInput: '))
        
    if in_mode == '1':
        ult.pure_rgb(pixels)
    
    elif in_mode == '2':
        ult.black_white(pixels)
        
    elif in_mode == '3':
        ult.random_color(pixels)
        
    elif in_mode == '4':
        ult.invert(pixels)
        
    elif in_mode == '5':
        ult.inverted_art(pixels, width)
        
    elif in_mode == '6':
        colors = ['red', 'green', 'blue']
        in_color = None
        
        while not in_color in colors:
            in_color = str(input('\nInput the wanted chanel (red, green, blue): '))
            
        ult.only_color(pixels, in_color)
        
    elif in_mode == '7':
        heightmap.color_height(pixels)

# main
get_pixels(img_path)

mode(pixels)

new_image(width, height)

print('new Image created')

