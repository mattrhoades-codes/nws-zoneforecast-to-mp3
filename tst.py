# I'm a n00b and there is probably a lot of stuff that isn't perfect, please leave comments!
# Python 2.7
import urllib2
import json
# 3d party lib: http://www.voicerss.org/sdk/python.aspx
import voicerss_tts

# fetch and load JSON from NWS API for zone forecast product, your product can be found:
# https://www.weather.gov/pimar/PubZone
response = urllib2.urlopen('https://api.weather.gov/zones/PUBLIC/ORZ511/forecast')
data = json.load(response)

# Iterate over zone forecast for number of periods (y) ie; Rest of Today, Tonight, Monday, Monday Night, Tuesday = 5
# Print those forecast periods to a text file, followed by new lines
def weather():
    x = -1
    y = 5
    for i in range(y):
        x += 1
        write_to.write(data['periods'][x]['name'])
        write_to.write("\n")
        write_to.write(data['periods'][x]['detailedForecast'])
        write_to.write("\n")

# Open file "forecast.txt" for writing, call function above, close file, open file,  read full file.
write_to = open("forecast.txt", "w")
weather()
write_to.close()
write2 = open("forecast.txt", 'r')
guts = write2.read()

# Direct example from voicerss.org, substituted the read file for a text string in 'src'
# Uses voicerss_tts API wrapper see imports and dependencies: http://www.voicerss.org/sdk/python.aspx
# Brings back file in MP3 format from voicerss
voice = voicerss_tts.speech({
    'key': <YOUR API KEY HERE>,
    'hl': 'en-us',
    'src': guts ,
    'r': '0',
    'c': 'mp3',
    'f': '44khz_16bit_stereo',
    'ssml': 'false',
    'b64': 'false'
})

newFile = open("voicerss.mp3", "wb")
newFile.write(voice['response'])
newFile.close()

