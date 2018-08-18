#!/bin/bash

# no multiple connections: needs to improve
while true; do
    line="$(netcat -l -p 10000)"
    notify-send -- "Received Message" "$line"
done
