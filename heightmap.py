
def color_height(pixels: list):
    for pixel in pixels:

        brightness = pixel.r / 255.0

        if pixel.r > 250:
            base_color = (245, 243, 238)  # White
            
        elif pixel.r > 210:
            base_color = (155, 155, 155)  # Gray
            
        elif pixel.r > 140:
            base_color = (155, 105, 70)   # Brown
            
        elif pixel.r > 90:
            base_color = (130, 85, 50)    # dark brown
            
        elif pixel.r > 2:
            base_color = (80, 115, 45)    # dark Green
            
        elif pixel.r < 2:
            base_color = (0, 109, 190)        # blue 

        shade = 0.5 + brightness * 0.7

        pixel.color = tuple(
            max(0, min(255, int(channel * shade)))
            for channel in base_color
        )
        
    print('\nHeightmap Colored')