from PIL import Image
import math, argparse
input_image = Image.open("./sample.jpg")


density = "Ñ@#W$9876543210?!abc;:+=-,._ "
#density = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

pixel_map = input_image.load()
width, height = input_image.size
# greyscale = 0

def mapping(n, start1, stop1, start2, stop2):
    return ((n-start1)/(stop1-start1))*(stop2-start2)+start2

text = 0
asciimage = ""

print('generating ASCII art...')

for i in range(width):
    for j in range(height):
        r, g, b = input_image.getpixel((j, i))
        grayscale = (0.299*r + 0.587*g + 0.114*b)
        pixel_map[j, i] = (int(grayscale), int(grayscale), int(grayscale))
        text = math.floor(mapping(grayscale, 0, 255, 0, len(density)))
        asciimage += density[text - 1]
    asciimage += "\n"

# Si queremos copiar directamente de la consola el output por comodidad
#print(asciimage)

# set output file
outFile = 'out.txt'

print('Done!!')

# open file
f = open(outFile, 'w')

f.write(asciimage)

# cleanup
f.close()

# Si queremos guardar la img en escala de grises
#input_image.save("./grayscale.png", format="png")