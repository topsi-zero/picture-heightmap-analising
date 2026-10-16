from PIL import Image

new = Image.new("RGB", (10, 10), color = (0,0,0))

new.putpixel((2,2), (200, 200, 10))
new.putpixel((4,4), (10, 200, 200))
new.putpixel((6,6), (200, 10, 200))


new.save("assets/testing.png")