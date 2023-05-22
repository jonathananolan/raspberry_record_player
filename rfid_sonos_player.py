from PiicoDev_RFID import PiicoDev_RFID
from PiicoDev_Unified import sleep_ms

import time
import requests                                 

rfid = PiicoDev_RFID()

# sonos group of speakers to play
sonos_group = "Bedroom"
sonos_user = "James"

# sleep times (ms)

# time between rfid record calls to read
rfid_read_cycle = 1000
# time between loading the album and playing it
play_delay = 1000
# once an album has started, wait this time additionally before subsequent rfid reads
start_play_delay = 2000

# time between rfid reads to consider that a record has been removed. used 
# to identify cases where a record has been placed on the turntable a second time.
record_removed_delay = 10000

record_string = ""
print('Hold tag near the PiicoDev RFID Module to read some text')
load = requests.get(f"http://localhost:5005/{sonos_user}/musicsearch/library/load")    
print(load)

# datetime when last read
time_last_read= time.time()*1000

while True:
    # boolean representing whether a different record is on the turntable
    different_record = True
    # boolean represeting whether the record has been replaced
    same_record_replaced = False

    # blocks until text is read on RFID tag
    record_string_new = rfid.readText()
    time_current_read = time.time()*1000
    time_since_last_read = time_current_read - time_last_read
    print(f"Time since last read: {time_since_last_read}ms")
    # check if current record is the same
    if record_string_new == record_string:
        different_record = False
        # given current record is the same, lets see whether a read has occurred in the last read cycle
        # if it hasn't, this means that the record was removed and replaced
        if time_since_last_read > record_removed_delay:
            same_record_replaced = True

    time_last_read = time_current_read
    
    print("string_new " +record_string_new)
    print("string " + record_string)
    print(f"Different record: {different_record}")
    print(f"Same record replaced: {same_record_replaced}")
    sleep_ms(rfid_read_cycle)

    if record_string_new != "" and (different_record or same_record_replaced):
        record_string = rfid.readText()
        print('Text in tag:')
        print(record_string)

        response = requests.get(f"http://localhost:5005/{sonos_group}/{record_string}")        
        # only play when successful
        if response.status_code == 200:     # To print http response code  
            sleep_ms(play_delay)
            response = requests.get(f"http://localhost:5005/{sonos_group}/play")        # To execute get request 
        else:
            print(response.status_code)
            print(response.text)            # To print formatted JSON response 

        sleep_ms(start_play_delay)

