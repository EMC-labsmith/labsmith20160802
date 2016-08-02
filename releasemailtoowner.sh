#!/bin/bash

machine=$1
port=$2
tomail=$3
status=$4
echo -e " Please make sure $machine is in good status. Current machine status:\n\n" \
        "$status\n"\ > /home/joe/labsmith_backup/releasetoownerfile
mail -s "You have released $machine" $tomail < /home/joe/labsmith_backup/releasetoownerfile


