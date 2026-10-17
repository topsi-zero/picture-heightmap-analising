
def color_height(pixels: list):
    print('\n')
    colored_pixel = 0
    max_pixels = len(pixels)

    for pixel in pixels:
        colored_pixel += 1

        brightness = pixel.r / 255.0

        if pixel.r > 250:
            base_color = (245, 243, 238)  # White
            
        elif pixel.r > 210:
            base_color = (155, 155, 155)  # Gray
            
        elif pixel.r > 140:
            base_color = (155, 105, 70)   # Brown
            
        elif pixel.r > 90:
            base_color = (130, 85, 50)    # dark brown
            
        elif pixel.r > 1:
            base_color = (80, 115, 45)    # dark Green
            
        else:
            base_color = (0, 109, 190)        # blue 

        shade = 0.5 + brightness * 0.7

        pixel.color = tuple(
            max(0, min(255, int(channel * shade)))
            for channel in base_color
        )

        print(f'\r[ {colored_pixel} / {max_pixels} ] pixels colored', end='', flush=True)
        
    print('\n\nHeightmap Colored\n')