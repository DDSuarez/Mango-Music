""" Code that uses IBM Watson to convert lyrics to mood """

import requests
import time
import serial
import time
from PyLyrics import *

def twitterGrab():
    username = "c9fd668e-4e8e-4a9f-97ff-524b3282f8a9"
    password = "VTw4ScwxgI"
    host = "cdeservice.mybluemix.net"
    port = 443
    url = "https://c9fd668e-4e8e-4a9f-97ff-524b3282f8a9:VTw4ScwxgI@cdeservice.mybluemix.net"
    header = {"content-type": "text/plain"}
    resp = requests.get(url, auth=(username, password), headers=header)

# Returns the percentages of mood found in a text
def moods(text):
    url = 'https://watson-api-explorer.mybluemix.net/tone-analyzer/api/v3/tone?version=2016-05-19'
    data = text
    username = '7144acc5-8b6b-4721-98c0-7696a547a450'
    password = 'W0LzbWyPDmsl'
    header = {"content-type": "text/plain"}
    resp = requests.post(url, data=data, auth=(username, password), headers=header)
    if resp.status_code != 200:
        print(resp.status_code)

    respJson = resp.json()
    respDocTone = respJson['document_tone']
    respToneCat = respDocTone['tone_categories']
    respTones = respToneCat[0]
    respInTones = respTones['tones']

    # opening a serial port to send data to the Arduino
    ser = serial.Serial('/dev/ttyUSB0', 9600)
    time.sleep(2)

    # write to serial
    thin = '{:,.2f} {:,.2f} {:,.2f} {:,.2f} {:,.2f}'.format(respInTones[0]['score'], respInTones[1]['score'],
    respInTones[2]['score'], respInTones[3]['score'],respInTones[4]['score'])

    print(thin)

    ser.write(thin)
    
    ser.write(thin)
    ser.close()

    # Big thanks to Matt

artist = "Dance Gavin Dance"
song = "Uneasy Hearts Weigh the Most"

print(PyLyrics.getLyrics(artist, song))
moods(PyLyrics.getLyrics(artist, song))

# Supposed to return the lyrics to the song name passed in as a parameter
# Needs to return a concatnated string of lyrics, search is not too efficient,
# needs to be made efficient
def binglyrics(search):
    url = "https://api.cognitive.microsoft.com/bing/v5.0/news/search?q=" \
    + search + "&count=10&offset=0&mkt=en-us&safeSearch=Moderate"

    header = {'Host': 'api.cognitive.microsoft.com', \
    'Ocp-Apim-Subscription-Key': 'a7c37c0e2b124cfe8e74f4824693d0f6'}

    resp = requests.get(url, headers=header)
    if resp.status_code != 200:
        print(resp.status_code)

    descriptionList = []

    respJson = resp.json()
    print(respJson)
    respVal = respJson['value']
    for a in range(0,len(respVal)):
        print(respVal[a]['description'])
        descriptionList.append(respVal[a]['description'])
