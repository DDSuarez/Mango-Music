""" Code that uses IBM Watson to convert lyrics to mood """

import requests
import time
import serial
import time
from PyLyrics import *

def twitterDB(search):
    username = "235c39c8-714b-440d-9415-57876c2f9d02-bluemix"
    password = "44629e5f840cd905917778926e8846b37658a3c4bd626aaac6f6f706d0acce27"
    host = "235c39c8-714b-440d-9415-57876c2f9d02-bluemix.cloudant.com"
    port = 443
    url = "235c39c8-714b-440d-9415-57876c2f9d02-bluemix.cloudant.com/nodered/_all_docs"
    header = {"Host": host, "Port": 443, "Authorization": "Basic MjM1YzM5YzgtNzE0Yi00NDBkLTk0MTUtNTc4NzZjMmY5ZDAyLWJsdWVtaXg6NDQ2MjllNWY4NDBjZDkwNTkxNzc3ODkyNmU4ODQ2YjM3NjU4YTNjNGJkNjI2YWFhYzZmNmY3MDZkMGFjY2UyNw=="}
    resp = requests.get(url, auth=(username, password), headers=header)

    print(resp)

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

#print(PyLyrics.getLyrics(artist, song))
#moods(PyLyrics.getLyrics(artist, song))
twitterDB("mangohacks")

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
