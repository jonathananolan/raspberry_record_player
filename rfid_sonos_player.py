from PiicoDev_RFID import PiicoDev_RFID
from PiicoDev_Unified import sleep_ms
import requests                                 

rfid = PiicoDev_RFID()

# sonos group of speakers to play
sonos_group = "Bedroom"
sonos_user = "James"

record_string = ""
print('Hold tag near the PiicoDev RFID Module to read some text')
load = requests.get(f"http://localhost:5005/{sonos_user}/musicsearch/library/load")    
print(load)

while True:
    record_string_new = rfid.readText()
    print("string_new " +record_string_new)
    print("string " + record_string)
    sleep_ms(1000)
    if record_string != record_string_new and record_string_new != "":
        record_string = rfid.readText()
        print('Text in tag:')
        print(record_string)

        response = requests.get(f"http://localhost:5005/{sonos_group}/{record_string}")        
        # only play when successful
        if response.status_code == 200:     # To print http response code  
            sleep_ms(1000)
            response = requests.get(f"http://localhost:5005/{sonos_group}/play")        # To execute get request 
        else:
            print(response.status_code)
            print(response.text)            # To print formatted JSON response 

        sleep_ms(2000)

