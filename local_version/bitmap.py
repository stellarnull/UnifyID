from PIL import Image
import bits

X = 128
Y = 128

img = Image.new("RGB", (X, Y), "white")

random_org = bits.GenRand()
bites = random_org.get_bytes_from_local()

assert len(bites) > X*Y*3

index = 0

for x in range(X):
    for y in range(Y):
        img.putpixel((x, y), tuple(ord(i) for i in bites[index:index+3]))
        index += 3

with open('randomImage.BMP', 'wb') as fs:
    img.save(fs, 'BMP')
