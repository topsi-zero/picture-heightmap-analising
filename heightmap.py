palette = [
    (0,   (100, 135, 65)),   # Muted olive green
    (140, (100, 135, 65)),   # Green ends
    (175, (155, 105, 70)),   # Brown
    (220, (155, 155, 155)),  # Gray
    (245, (245, 243, 238)),  # White
]

def color_height(pixels: list):
    for pixel in pixels:
        for i in range(len(palette) -1):
            h0, c0 = palette[i]
            h1, c1 = palette[i + 1]
            
            if h0 <= pixel.g <= h1:
                t = (pixel.g - h0) / (h1 -h0)
                
                pixel.r = int(c0[0] + t * (c1[0] - c0[0]))
                pixel.g = int(c0[1] + t * (c1[1] - c0[1]))
                pixel.b = int(c0[2] + t * (c1[2] - c0[2]))
                
                pixel.set_color()
