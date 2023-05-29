#!/bin/bash

# derived from https://github.com/Pyrestone/python-service-example/blob/master/install.sh
service_name="rfid_sonos_player"

# Require sudo
if [ $EUID != 0 ]; then
    sudo "$0" "$@"
    exit $?
fi

echo "adding service to /lib/systemd/system/..."
# copy service config file to systemd
cp ${service_name}.service /lib/systemd/system/
# set permissions: owner can read/write, group can read, others can read. none can execute
chmod 644 /lib/systemd/system/$service_name.service
echo "done"

echo "starting and enabling $service_name service..."
systemctl daemon-reload
systemctl start $service_name
systemctl enable $service_name
echo "done"

echo "$service_name installed sucessfully!"
