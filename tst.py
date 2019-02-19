# I'm a n00b and there is probably a lot of stuff that isn't perfect, please leave comments!
import requests
import json
import os
# 3d party lib: http://www.voicerss.org/sdk/python.aspx
import voicerss_tts

def main():
    report_filename = generate_weather_report()
    voice_filename = generate_voice_report(report_filename)
    print('SUCCESS: {} created from {}'.format(voice_filename, report_filename))

# Funtion to geneate text based weather report
def generate_weather_report(number_of_periods=5):
    # fetch and load JSON from NWS API for zone forecast product, your product can be found:
    # https://www.weather.gov/pimar/PubZone
    url = 'https://api.weather.gov/zones/PUBLIC/ORZ511/forecast'
    report_filename = 'forecast.txt'
    
    response = requests.get(url)
    data = response.json()

    # Iterate over zone forecast for number of periods (i) ie; Rest of Today, Tonight, Monday, Monday Night, Tuesday = 5
    # Print those forecast periods to a text file, followed by new lines

    # Open file "forecast.txt" for writing, call function above, close file, open file,  read full file.
    with open(report_filename, "w") as forecast:
        # Set number of periods of forecast you would like

        for i in range(number_of_periods):
            forecast.write(data['periods'][i]['name'])
            forecast.write("\n")
            forecast.write(data['periods'][i]['detailedForecast'])
            forecast.write("\n")
    
    return report_filename

# Function to create mp3 voice report from text file
def generate_voice_report(filename):

    voice_filename = 'voicerss.mp3'

    with open(filename, 'r') as forecast:
        src = forecast.read()

    # Direct example from voicerss.org, substituted the read file for a text string in 'src'
    # Uses voicerss_tts API wrapper see imports and dependencies: http://www.voicerss.org/sdk/python.aspx
    # Brings back file in MP3 format from voicerss
    # Get API key from environment variable
    voice_rss_api_key = os.environ['voice_rss_api_key']

    voice = voicerss_tts.speech({
        'key': voice_rss_api_key,
        'hl': 'en-us',
        'src': src ,
        'r': '0',
        'c': 'mp3',
        'f': '44khz_16bit_stereo',
        'ssml': 'false',
        'b64': 'false'
    })

    with open(voice_filename, "wb") as newFile:
        newFile.write(voice['response'])

    return voice_filename

if __name__ == '__main__':
    main()