# Raspberry Pi Record Player

# How to print...

Details for the fabrication are available here: 

https://www.printables.com/model/673426-raspberry-pi-record-player

## Start on boot

To have the record player start on boot, you can install it as a systemd service,
with the service defined in `rfid_sonos_player.service`. A bash setup script `setup_service.sh`
can then be run to install, enable, and start the service.

Set permissions to execute the service setup script, then execute the script

```bash
chmod u+x setup_service.sh
./setup_service.sh
```

## Restart daily

To restart the rpi daily you can use cron. To edit the cron file:
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


