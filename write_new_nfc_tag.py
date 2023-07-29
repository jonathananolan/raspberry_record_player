from PiicoDev_RFID import PiicoDev_RFID
from PiicoDev_Unified import sleep_ms
import requests
import csv

# Initialize RFID
rfid = PiicoDev_RFID()

# sonos room to play test sound on
sonos_room = "Sonos Move"
play_delay = 100

def csv_lookup(lookup_key):
    file_path = '/home/pi/raspberry_record_player/lookup_table.csv'  # Define the csv file path here
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['key'] == lookup_key:
                if row['local'] == '1':
                    # Replace spaces with "+" in both "artist" and "album" fields
                    artist = row['artist'].replace(' ', '+')
                    album = row['album'].replace(' ', '+')
                    return artist + "+" + album
                else:
                    return "spotify/now/spotify:album:" + row['spotify_album_uri']
    return lookup_key  # return the full key if nothing is found

while True:
    # Take the album_key as an input
    album_key = input("Enter the album key: ")
    album_string = csv_lookup(album_key)

    load = requests.get(f"http://localhost:5005/{sonos_room}/musicsearch/library/load")        
    response = requests.get(f"http://localhost:5005/{sonos_room}/{album_string}")        
    # only play when successful
    if response.status_code == 200:     
        sleep_ms(play_delay)
        response = requests.get(f"http://localhost:5005/{sonos_room}/play")
    else:
        print(response.status_code)
        print(response.text)  # To print formatted JSON response 

    print(album_string)
    success = rfid.writeText(album_key)
    if success:
        data = rfid.readText()
        print('Text in tag:', data)
        
        if data == album_key:
            print('Success')
            successful_write = True
        else:
            print("Write failed - try again")
    sleep_ms(10)
