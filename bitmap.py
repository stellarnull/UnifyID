import requests
import re
from PIL import Image
import random
import numpy as np
import util

SIZE = 128

def createColor():
    '''
    returns numpy array representing a color in the image
    '''
    pixelsStillNeeded = SIZE * SIZE #the number of pixels in 128x128 image
    minRand = 0
    maxRand = 255
    col = SIZE
    base = 2
    midList = []
    while pixelsStillNeeded > 0:
        if (pixelsStillNeeded - 10000) > 0:
            requestNumber =  10000
        else:
            requestNumber = pixelsStillNeeded #limits random numbers requested since the requests are limited to 10000 random numbers
        pixelsStillNeeded -= requestNumber
        # genericURL = "https://www.random.org/integers/?num={0}&min={1}&max={2}&col={3}&base={4}&format=plain&rnd=new"
        # url = genericURL.format(requestNumber, minRand, maxRand, col, base)
        url = util.createURL(requestNumber,minRand, maxRand, col, base) 
        # print url
        response = requests.get(url)
        if response.status_code != 200:
            print('Could not request bits due to a ['
            + str(response.status_code)
            + '] error')
            exit()
        print response
        listOfNumbers = util.decodeResponse(response)
        midList += listOfNumbers #keeps a list of all the random numbers
        # print len(listOfNumbers)
    finalArray = np.array(midList)
    return np.reshape(finalArray, (SIZE, SIZE))

def populateList(num):
    '''
    outputs a list with num random numbers
    this was used so as not to waste api calls to the website
    not used in final 
    '''
    final = []
    for i in range(num):
        ran = random.randint(0,255)
        bi = str(bin(ran))
        final.append(bi[2:])
    return final
    
def createImage(red, blue, green):
    '''
    takes in 3 np arrays of size (128,128) representing
    red blue and green colors in the image
    '''
    imageArray = np.zeros([SIZE,SIZE,3])
    imageArray[:,:,0] = red
    imageArray[:,:,1] = blue
    imageArray[:,:,2] = green

    imageArray = np.uint8(imageArray)

    img = Image.fromarray(imageArray)
    img.save("randomImage.BMP")
    img.show()




def main():
    r = createColor()
    g = createColor()
    b = createColor()
    createImage(r,g,b)

if __name__ == "__main__":
    main()