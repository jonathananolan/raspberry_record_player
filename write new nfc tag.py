from PiicoDev_RFID import PiicoDev_RFID
from PiicoDev_Unified import sleep_ms

rfid = PiicoDev_RFID()

#local files
myString = 'musicsearch/library/album/Bennies+Better+off+dread' # You can store up to 143 characters on a tag
#spotify
#myString = 'spotify/now/spotify:album:6FJxoadUE4JNVwWHghBwnb'

print(myString)

('Hold tag near the PiicoDev RFID Module to write album to it.')
print('')

while True:
    success = rfid.writeText(myString)
    if success:
        data = rfid.readText()
        print('Text in tag:')
        print(data)
        break
    sleep_ms(10)