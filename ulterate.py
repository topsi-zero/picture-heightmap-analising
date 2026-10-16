import random as rd


def pure_rgb(pixels: list):
    
    for pixel in pixels:        
        if pixel.r > pixel.g and pixel.r > pixel.b:
            pixel.g, pixel.b = 0, 0
            
        elif pixel.g > pixel.r and pixel.g > pixel.b:
            pixel.r, pixel.b = 0, 0
            
        elif pixel.b > pixel.r and pixel.b > pixel.g:
            pixel.r, pixel.g = 0, 0
            
        pixel.set_color()
    
    print('Pixelcolor changed to pure RGB')
    
def black_white(pixels: list):
    
    for pixel in pixels:
        if pixel.r > pixel.g and pixel.r > pixel.b:
            pixel.g, pixel.b = pixel.r, pixel.r
        
        elif pixel.g > pixel.r and pixel.g > pixel.b:
            pixel.r, pixel.b = pixel.g, pixel.g
            
        elif pixel.b > pixel.r and pixel.b > pixel.g:
            pixel.g, pixel.r = pixel.b, pixel.b
            
        pixel.set_color()
            
    print('Pixelcolor changed to black and white')
    
def random_color(pixels: list):
    for pixel in pixels:
        r_num = rd.randint(1,3)
        
        if r_num == 1:
            pixel.g, pixel.b = 0, 0
            
        elif r_num == 2:
            pixel.r, pixel.b = 0, 0
            
        else:
            pixel.r, pixel.g = 0, 0
            
        pixel.set_color()
        
def invert(pixels: list):
    strength = int(input('Input an intiger strength modifier: '))
    
    for pixel in pixels:
        pixel.r = 255 - pixel.r + strength
        pixel.g = 255 - pixel.g + strength
        pixel.b = 255 - pixel.b + strength
        
        if pixel.r > 255:
            pixel.r = 255
            
        elif pixel.r < 0:
            pixel.r = 0
            
        if pixel.g > 255:
            pixel.g = 255
            
        elif pixel.g < 0:
            pixel.g = 0
            
        if pixel.b > 255:
            pixel.b = 255
            
        elif pixel.b < 0:
            pixel.b = 0
            
        pixel.set_color()
    
    print('Pixelcolor inverted')
        
def inverted_art(pixels: list, width):
            
    transition_width = 0.2 * width

    start = (width - transition_width) / 2
    end = (width + transition_width) / 2

    for pixel in pixels:
        if pixel.x < start:
            continue

        t = min(1.0, max(0.0, (pixel.x - start) / transition_width))
        factor = t * t * (3 - 2 * t)

        r, g, b = pixel.r, pixel.g, pixel.b

        inv_r = 255 - r
        inv_g = 255 - g
        inv_b = 255 - b

        pixel.r = int(r * (1 - factor) + inv_r * factor)
        pixel.g = int(g * (1 - factor) + inv_g * factor)
        pixel.b = int(b * (1 - factor) + inv_b * factor)
        
        pixel.set_color()
    
    print('Pixelcolor half inverted')
    
def only_color(pixels: list, color: str):
    for pixel in pixels:
        if color == 'red':
            pixel.color = (pixel.r, 0, 0)
            
        elif color == 'green':
            pixel.color = (0, pixel.g, 0)
            
        elif color == 'blue':
            pixel.color = (0, 0, pixel.b)
            
    print(f'Pixelcolor changed  to {color}.')
    
    
    
    