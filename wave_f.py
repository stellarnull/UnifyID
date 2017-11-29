import wave
import requests
import re
import numpy as np
import util

SIZE = 44100

def createRand(num = 1, min_int = 1, max_int = 2, col = 1, base = 16, format_return='plain', rnd='1'):
    '''
    returns numpy array representing a color in the image
    '''
    pixelsStillNeeded = num #the number of pixels in 128x128 image
    minRand = min_int
    maxRand = max_int
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
        print url
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
    return finalArray

def main():
	samplelength = SIZE*3
	#misspelled to not conflict with builtin 'bytes'
	rands = createRand(samplelength, 0, 0xFF, 1, 16)

	wf = wave.open('output.wav', 'wb')
	wf.setparams((1, 1, SIZE, 0, 'NONE', 'not compressed'))
	wf.writeframes(rands)
	wf.close()

if __name__ == "__main__":
    main()