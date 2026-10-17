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

folder = str(input('\ninput folder structure and name/s, if directly in assets folder press enter (-> foldername or foldername/subfolder <-)\nInput: assets/'))
filename = str(input(f'\ninput the filename including suffix (-> filename.suffix <-)\nInput: assets/{folder}/'))

name = filename.split('.')

name = name[0]

img_path = "assets/" + folder + '/' + filename

print(f'\nscanning image: assets/{folder}/{filename}\n')

try:
    img = Image.open(img_path)

except FileNotFoundError:
    print(f'\n\nError: No such FILE or DIRECTORY: assets/{folder}/{filename}\n\n')
    exit()

width, height = img.size

# definitions

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

            print(f'\r[ {pixelcount} / {width * height} ] pixels analised', end='', flush=True)
            
    
                        
def new_image(width, height, option: bool = False):
    global filename
    written_pixels = 0
    
    output_img = Image.new("RGB", (width, height), color = (0,0,0))
    
    for pixel in pixels:
        output_img.putpixel((pixel.x, pixel.y), pixel.color)

        written_pixels += 1
        print(f'\r[ {written_pixels} / {len(pixels)} ] pixels written', end='', flush=True)

    output_img.save(f"output/{name}_changed.png" if not option else f"output/{name}_heightmap.png")

    print('\n\nnew image saved')
    
    
def mode(pixels):
    global width
    
    allowed_answers = ['1', '2', '3', '4', '5', '6', '7']
    in_mode: str = None
    
    while not in_mode in allowed_answers:
        in_mode = str(input('\n\nChose your option (-> number <-): \n(1) pure RGB\n(2) Black and White \n(3) Random Color \n(4) Invert \n(5) Half invert \n(6) single color channel \n\nHeightmap options: \n(7) colored heightmap \nInput: '))

    print('\n')
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

new_image(width, height, option = True if mode == 7 else False)