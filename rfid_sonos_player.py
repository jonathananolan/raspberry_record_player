from PiicoDev_RFID import PiicoDev_RFID
from PiicoDev_Unified import sleep_ms
import requests                                 # To use request package in current program 

rfid = PiicoDev_RFID()

myString = "test"
print('Hold tag near the PiicoDev RFID Module to read some text')
load = requests.get("http://localhost:5005/Jonathan/musicsearch/library/load")        

while True:
    myString_new = rfid.readText()
    print("string_new " +myString_new)
    print("string " + myString)
    sleep_ms(1000)
    if myString != myString_new and myString_new != "":
        myString = rfid.readText()
        response = requests.get("http://localhost:5005/Bedroom/" + myString)        # To execute get request 
        sleep_ms(1000)
        response = requests.get("http://localhost:5005/Bedroom/play")        # To execute get request 
        print(response.status_code)     # To print http response code  
        print(response.text)            # To print formatted JSON response 
        print('Text in tag:')
        print(myString)
        sleep_ms(2000)

