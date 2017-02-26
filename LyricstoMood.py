""" Code that uses IBM Watson to convert lyrics to mood """

import requests
import time
import serial
<<<<<<< HEAD
import time
from PyLyrics import *
=======
<<<<<<< HEAD
import time
from PyLyrics import *
=======
import string
import re
import urllib

from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

"""def lyrics(artist,song):
    artist = artist.lower()
    song = song.lower()
    artist = re.sub('[^A-Za-z0-9]+', "", artist)
    song = re.sub('[^A-Za-z0-9]+', "", song)
    raw_html = urllib.urlopen("http://azlyrics.com/lyrics/"+str(artist)+"/"+str(song)+".html")
    html_copy = str(raw_html.read())
    split = html_copy.split('<!-- Usage of http://azlyrics.com     content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->',1)
    split_html = split[1]
    split = split_html.split('</div>',1)
    lyrics = split[0]
    lyrics = re.sub('(<.*?>)',"",lyrics)
    print(lyrics)
    return lyrics """

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

>>>>>>> 91630ee5222fb349b50c93260fe51e3070ca5d60
>>>>>>> PyLyrics

# Supposed to return the percentages of mood found in a text
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
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> PyLyrics

    print(thin)

    ser.write(thin)
    
<<<<<<< HEAD
    ser.write(thin)
=======
=======
    ser.write(thin)
>>>>>>> 91630ee5222fb349b50c93260fe51e3070ca5d60
>>>>>>> PyLyrics
    ser.close()

    # Big thanks to Matt

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> PyLyrics
artist = "Dance Gavin Dance"
song = "Uneasy Hearts Weigh the Most"

print(PyLyrics.getLyrics(artist, song))
moods(PyLyrics.getLyrics(artist, song))
<<<<<<< HEAD
=======
=======
#print(similar("Dance Gavin Danve And They Say I Invented Times New Roman", "Dance Gavin DanveAnd They Say I Invented Times New Roman"))
#moods("I am sad.")
binglyrics("Dance Gavin Dance lyrics")
#moods(lyrics("Dance Gavin Danve", "And They Say I Invented Times New Roman"))
>>>>>>> 91630ee5222fb349b50c93260fe51e3070ca5d60
>>>>>>> PyLyrics
