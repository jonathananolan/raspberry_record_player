# Raspberry Pi Record Player

## Start on boot

To have the record player start on boot, you can install it as a systemd service,
with the service defined in `rfid_sonos_player.service`. A bash setup script `setup_service.sh`
can then be run to install, enable, and start the service.

Set permissions to execute the service setup script, then execute the script

```bash
chmod u+x setup_service.sh
./setup_service.sh
```

## Debugging

### Node Sonos API

Run `pm2 log` to see requests coming through the Node Sonos API

### Record player service

Run `journalctl -u rfid_sonos_player` to see the output of the python record player


