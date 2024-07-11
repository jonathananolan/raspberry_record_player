# Raspberry Pi Record Player

This repo lets you create a tiny record player that controls your SONOS devices. 

![image](https://github.com/jonathananolan/raspberry_record_player/assets/10514600/4a78a7c3-62a3-41a4-84bb-1abd214ecd45)

# How to fabricate the device

Details for the fabrication are available here: 

https://www.printables.com/model/673426-raspberry-pi-record-player

# Set up
Install Raspberry pi etc, then clone this package by typing 

```
git clone https://github.com/jonathananolan/raspberry_record_player
```

Then edit line 10 of ```rfid_sonos_player.py``` to make sure it reflects the group name of the SONOS player you want to connect to (you can find this out in your SONOS app) 

To make the record player start on boot, you can install the python file as a systemd service,
with the service defined in `rfid_sonos_player.service`. A bash setup script `setup_service.sh`
can then be run to install, enable, and start the service.

Set permissions to execute the service setup script, then execute the script

```bash
chmod u+x setup_service.sh
./setup_service.sh
```

# Creating new records
You can assign records to a given RFID tag by entering their details in the lookup_table.csv file. If local is set to 1 then the device will search for the album on your local sonos system, otherwise it will use the spotify URI. Spotify URIs can be found by searching for the album in the spotify web-app and looking at the URL.

"local" playback is experimental and you may need to know some python to fix it. Pull requests welcomed! 

write_new_nfc_tag.py enables you to write the 'key' for each album to an RFID tag. 

## Restart daily

Reliability is improved when you set the Raspberry pi to restart daily. To do this you can use cron. To edit the cron file:
```bash
crontab -e
```

Then insert something like the following (this restarts every day at 4am)
```bash
# m h  dom mon dow   command
  0 4   *   *   *    /usr/bin/sudo /sbin/shutdown -r now
```

## Debugging

### Node Sonos API

Run `pm2 log` to see requests coming through the Node Sonos API

### Record player service

Run `journalctl -u rfid_sonos_player` to see the output of the python record player


