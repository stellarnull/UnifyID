from PIL import Image

import bits


X = 128
Y = 128

im = Image.new("RGB", (X, Y), "white")

random_org = bits.RandomOrg()
#misspelled to not conflict with builtin 'bytes'
bites = random_org.get_bytes_from_local()

assert len(bites) > X*Y*3

index = 0

for x in range(X):
    for y in range(Y):
        im.putpixel((x, y), tuple(ord(i) for i in bites[index:index+3]))
        index += 3

with open('output.png', 'wb') as f:
    im.save(f, 'PNG')
