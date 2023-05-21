from PiicoDev_RFID import PiicoDev_RFID
from PiicoDev_Unified import sleep_ms
import requests

# spotify room to play test sound on
spotify_room = "Bedroom"

# define sonos search string for music stored in the library or provide a spotify album url

# local files
#album_string = 'musicsearch/library/album/cat+empire' # You can store up to 143 characters on a tag

# spotify
album_string = 'spotify/now/spotify:album:0YtYaaO0aipyeQl0xhAWTO'

rfid = PiicoDev_RFID()
load = requests.get(f"http://localhost:5005/{spotify_room}/musicsearch/library/load")        

print(album_string)
response = requests.get(f"http://localhost:5005/{spotify_room}/{album_string}")        # To execute get request 
print(response)
print(response.text)            # To print formatted JSON response 
print('Hold tag near the PiicoDev RFID Module to write album to it.')
print('')

while True:
    success = rfid.writeText(album_string)
    if success:
        data = rfid.readText()
        print('Text in tag:')
        print(data)
        break
    sleep_ms(10)


print("Pausing")
requests.get(f"http://localhost:5005/{spotify_room}/pause")
