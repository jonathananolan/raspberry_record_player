from PiicoDev_RFID import PiicoDev_RFID
from PiicoDev_Unified import sleep_ms
import requests                                 # To use request package in current program 

rfid = PiicoDev_RFID()
load = requests.get("http://localhost:5005/Living Room/musicsearch/library/load")        

#local files
myString = 'musicsearch/library/album/boomgates+double+natural' # You can store up to 143 characters on a tag
#spotify
#myString = 'spotify/now/spotify:album:6FJxoadUE4JNVwWHghBwnb'

print(myString)
response = requests.get("http://localhost:5005/Living Room/" + myString)        # To execute get request 
print(response)
print(response.text)            # To print formatted JSON response 
print('Hold tag near the PiicoDev RFID Module to write album to it.')
print('')

while True:
    success = rfid.writeText(myString)
    if success:
        data = rfid.readText()
        print('Text in tag:')
        print(data)
        break
    sleep_ms(10)
