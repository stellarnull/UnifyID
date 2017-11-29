import requests
import re
from PIL import Image
import random
import numpy as np


def createURL(nums, minRand, maxRand, col, base):
    '''
    creates a url to use in the api call to random.org
    takes in as parameters
    nums - the number of random numbers to be gotten from the website
    minRand - the minimum number that could possibly be generated
    maxRand - the maximum number that could possibly be generated
    col - the number of columns the data should be returned in
    base - the base of the random number
    '''
    originalString = "https://www.random.org/integers/?"
    originalString += "num=" + str(nums)
    originalString += "&min=" + str(minRand)
    originalString += "&max=" + str(maxRand)
    originalString += "&col=" + str(col)
    originalString += "&base=" + str(base) + "&format=plain&rnd=new"
    return originalString

def decodeResponse(response):
    '''
    input- api response in byte stream
    returns - list of random numbers from response
    '''
    mid = response.content.decode("utf-8")
    numbers = re.split(r"[\t\n]+",mid)
    while "" in numbers:
        numbers.remove("")
    return numbers